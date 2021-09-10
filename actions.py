# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
from math import sin, cos, atan2, ceil, sqrt
from typing import Any, Text, Dict, List, Union, Optional, Tuple
import logging
import re
import os
import requests
import csv
import collections

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, FormValidationAction
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, Restarted
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.types import DomainDict


logger = logging.getLogger(__name__)

URL_FLIGHT_EMISSION = "https://test-api.atmosfair.de/api/emission/flight"


def hyperlink_payload(tracker, message, title, url):
    return {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": message,
                "buttons": [
                    {
                        "type": "web_url",
                        "url": url,
                        "title": title,
                        "webview_height_ratio": "full",
                    }
                ],
            },
        }
    }


class AirportsKnowledgeBase(InMemoryKnowledgeBase):
    def load(self):
        def is_active(airport):
            return (
                airport["type"].endswith("_airport")
                and airport["scheduled_service"] == "yes"
            )

        self.data = {"airport": []}
        with open(self.data_file, "r", encoding="utf-8") as f:

            airports = csv.DictReader(f)
            for airport in airports:
                if is_active(airport):
                    self.data["airport"].append(airport)

    def find_airport_by_ref(self, airport_ref):
        for airport in self.data["airport"]:
            if airport["iata_code"] == airport_ref:
                return airport
        return None

    def find_airports_by_city_or_code(self, city):

        objects = self.data["airport"]
        city = city.lower()

        objects = list(
            filter(
                lambda obj: obj["municipality"].lower() == city
                or city == obj["iata_code"].lower(),
                objects,
            )
        )
        # sort airports by size
        sizes = ["large_airport", "medium_airport", "small_airport", "closed"]
        objects = sorted(objects, key=lambda a: sizes.index(a["type"]))

        # put US airports first
        objects = list(filter(lambda obj: obj["iso_country"] == "US", objects)) + list(
            filter(lambda obj: obj["iso_country"] != "US", objects)
        )
        return objects

    @staticmethod
    def flight_class_code(code):
        codes = {"economy": "Y", "premium": "W", "business": "B", "first": "F"}
        if code in codes:
            return codes[code]
        return "Y"

    @staticmethod
    def co2_kg_interpolation(distance_km, flight_class, include_rfi=True):
        # Values are roughly approximated with linear least-squares
        # regression on a few hundred sample flights.
        if include_rfi:
            # This includes RFI, as presented on Atmosfair website.
            co2_kg_per_km = {
                "economy": 0.52,
                "premium": 0.66,
                "business": 0.97,
                "first": 1.30,
            }.get(flight_class)
        else:
            # This does not include RFI
            co2_kg_per_km = {
                "economy": 0.18,
                "premium": 0.23,
                "business": 0.33,
                "first": 0.44,
            }.get(flight_class)

        if not co2_kg_per_km:
            raise ValueError("Invalid flight class")

        return co2_kg_per_km * distance_km

    @staticmethod
    def co2_kg_climatiq(distance_km, flight_class):
        if distance_km < 866:  # longest possible UK domestic flight
            emission_factor = "domestic-flight"
        elif (
            distance_km < 3700
        ):  # borderline between short and long international flights
            emission_factor = "short-haul-flight"
        else:
            emission_factor = "long-haul-flight"

        if distance_km >= 866:
            if flight_class == "business":
                emission_factor += "-business"
            elif flight_class == "economy":
                emission_factor += "-economy"

        payload = {
            "emission_factor": emission_factor,
            "parameters": {"distance": distance_km,},
        }
        headers = {
            "Authorization": f"Bearer {os.getenv('CLIMATIQ_API_KEY')}",
            "Content-Type": "application/json",
        }

        response = requests.post(
            "https://beta.api.climatiq.io/estimate", json=payload, headers=headers
        )
        if response.status_code != 200:
            raise ValueError(
                f"Couldn't fetch a CO2 estimate. Error code: {response.status_code}"
            )

        data = dict(response.json())
        return data.get("co2e")

    @staticmethod
    def co2_kg_atmosfair(departure_iata, destination_iata, flight_class):
        payload = {
            "username": "kundentest",
            "password": "kundentest",
            "flights": [
                {
                    "departure": departure_iata,
                    "arrival": destination_iata,
                    "passengerCount": 1,
                    "travelClass": AirportsKnowledgeBase.flight_class_code(
                        flight_class
                    ),
                }
            ],
        }

        response = requests.post(URL_FLIGHT_EMISSION, json=payload)
        data = dict(response.json())

        if data.get("status", "FAILURE") == "SUCCESS":
            return data.get("co2")

    @staticmethod
    def great_circle_distance_km(lat_a, lon_a, lat_b, lon_b):
        r = 6371.0  # The Earth's radius
        phi_1 = float(lat_a) * 3.14159 / 180.0
        phi_2 = float(lat_b) * 3.14159 / 180.0
        delta_phi = (float(lat_b) - float(lat_a)) * 3.14159 / 180.0
        delta_lam = (float(lon_b) - float(lon_a)) * 3.14159 / 180.0

        a = sin(delta_phi * 0.5) * sin(delta_phi * 0.5) + cos(phi_1) * cos(phi_2) * sin(
            delta_lam * 0.5
        ) * sin(delta_lam * 0.5)
        c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
        return ceil(r * c / 100.0) * 100

    def calculate_emissions(self, tracker, unit="short_tons"):
        departure_iata = tracker.get_slot("iata_departure")
        destination_iata = tracker.get_slot("iata_destination")
        flight_class = tracker.get_slot("travel_flight_class")

        if not departure_iata:
            raise ValueError("Departure IATA code unknown.")
        if not destination_iata:
            raise ValueError("Destination IATA code unknown.")
        if not flight_class:
            raise ValueError("Flight class unknown.")

        departure_airport = self.find_airport_by_ref(departure_iata)
        destination_airport = self.find_airport_by_ref(destination_iata)

        if not departure_airport:
            raise ValueError(
                f"Could not find departure airport with IATA code '{departure_iata}'"
            )
        if not destination_airport:
            raise ValueError(
                f"Could not find destination airport with IATA code '{departure_iata}'"
            )

        # Compute the great circle distance between the two airports
        lat_a = departure_airport["latitude_deg"]
        lon_a = departure_airport["longitude_deg"]
        lat_b = destination_airport["latitude_deg"]
        lon_b = destination_airport["longitude_deg"]
        distance_km = self.great_circle_distance_km(lat_a, lon_a, lat_b, lon_b)

        # co2_kg = self.co2_kg_interpolation(distance_km, flight_class)
        co2_kg = self.co2_kg_climatiq(distance_km, flight_class)
        if not co2_kg:
            raise ValueError("CO2 amount could not be calculated.")

        kilos_per_unit = {
            "kilograms": 1.0,
            "short_tons": 907.0,  # Used in the US
            "long_tons": 1016.0,  # Used in UK and Commonwealth
            "metric_tons": 1000.0,  # Used by sensible people
        }.get(unit)

        if not kilos_per_unit:
            raise ValueError(f"Unknown unit: '{unit}'")

        unit_string = "kg" if unit == "kilograms" else "tons"

        co2 = (f"{ceil(10 * co2_kg / kilos_per_unit) * 0.1:.1f} {unit_string}",)
        return co2


class StartAction(Action):
    """Initiates the conversation, based on the present scenario."""

    def name(self):  # type: () -> Text
        return "action_start"

    def __init__(self):
        pass

    def run(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]

        url = (
            f"https://rasa.com/carbon/index.html?"
            f"&rasaxhost=https://carbon.rasa.com"
            f"&conversationId={tracker.sender_id}"
            f"&destination=https://offset.earth%2F%3Fr%3D5de3ac5d7e813f00184649ea"
        )

        link_1_url = url + f"&label=link-1-clicked"
        link_2_url = url + f"&label=link-2-clicked"

        return [SlotSet("link_1_url", link_1_url), SlotSet("link_2_url", link_2_url)]


AIRPORT_KB = AirportsKnowledgeBase("data/airports.csv")


class ValidateAirTravelForm(FormValidationAction):
    def __init__(self):
        self.kb = AIRPORT_KB
        super(ValidateAirTravelForm, self).__init__()

    def name(self) -> Text:
        return "validate_airtravel_form"

    def validate_travel_departure(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        return self._location_to_slot_dict(slot_value, "departure")

    def validate_travel_destination(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        return self._location_to_slot_dict(slot_value, "destination")

    @staticmethod
    def _location_to_slot_dict(location: Text, kind: Text) -> Dict:
        """
        Given a location description, fill the appropriate slots
        for departure or destination ('kind')
        :param location: A city name or IATA code
        :param kind: "departure" or "destination"
        :return: Dict of two slots
        """
        if not location:
            return {}

        candidates = AIRPORT_KB.find_airports_by_city_or_code(location)
        if len(candidates) > 0:
            result = {
                f"travel_{kind}": candidates[0]["name"],
                f"iata_{kind}": candidates[0]["iata_code"],
            }
        else:
            result = {f"travel_{kind}": None, f"iata_{kind}": None}
        return result


class CalculateOffsets(Action):
    """Attempts to calculate CO2 usage and display link to purchase offsets."""

    def name(self) -> Text:
        return "action_calculate_offsets"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:

        url = tracker.get_slot("link_2_url")
        try:
            co2_in_tons = AIRPORT_KB.calculate_emissions(tracker, unit="short_tons")

        except ValueError as e:
            logger.error(f"calculate_emissions failed with: {e}")
            dispatcher.utter_message("Sorry, I was unable to calculate that.")
            return []

        departure_airport = tracker.get_slot("travel_departure")
        departure_iata = tracker.get_slot("iata_departure")
        destination_airport = tracker.get_slot("travel_destination")
        destination_iata = tracker.get_slot("iata_destination")
        travel_flight_class = tracker.get_slot("travel_flight_class")
        if True:
            message = (
                f"A one-way flight from {departure_airport} ({departure_iata}) to {destination_airport} ({destination_iata}) "
                f"in {travel_flight_class} class emits {co2_in_tons[0]} of CO2. "
                f"It would be amazing if you bought offsets for that carbon! "
                f"There are some great, UN-certified projects you can pick from."
            )
        if tracker.get_latest_input_channel() == "facebook":
            payload = hyperlink_payload(tracker, message, "Buy Offsets", url)
            dispatcher.utter_custom_json(payload)
        else:
            dispatcher.utter_message(message + f" [Buy Offsets]({url})")

        slots_to_set = [
            SlotSet("travel_departure"),
            SlotSet("iata_departure"),
            SlotSet("travel_destination"),
            SlotSet("iata_destination"),
            SlotSet("travel_flight_class"),
        ]

        return slots_to_set


class ExplainTypicalEmissions(Action):
    def name(self):
        return "action_explain_typical_emissions"

    def run(self, dispatcher, tracker, domain):
        url = tracker.get_slot("link_1_url")
        message = (
            "A typical 3 hour flight will emit almost a ton of CO2 per economy passenger. "
            "If you cannot avoid flying, you can buy offsets for that carbon here: "
        )
        if tracker.get_latest_input_channel() == "facebook":
            payload = hyperlink_payload(tracker, message, "Buy Offsets", url)
            dispatcher.utter_custom_json(payload)
        else:
            dispatcher.utter_message(message + f" [Buy Offsets]({url})")
        return []


class ActionDisclaimer(Action):
    """Utters privacy disclaimer."""

    def name(self):  # type: () -> Text
        return "action_disclaimer"

    def __init__(self):
        pass

    def run(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]

        url = "https://rasa.com/carbon-bot-privacy-policy/"
        message = (
            "Hello! Just a heads up - this bot is part of a research "
            "project and we intend to make the conversations publicly available "
            "to researchers. So please don't share any personal information!"
        )

        if tracker.get_latest_input_channel() == "facebook":
            payload = hyperlink_payload(tracker, message, "Privacy Policy", url)
            dispatcher.utter_custom_json(payload)
        else:
            dispatcher.utter_message(message + f" [Privacy Policy]({url})")
        return []


class ActionRestart(Action):
    """Restarts conversation."""

    def name(self):  # type: () -> Text
        return "action_restart"

    def __init__(self):
        pass

    def run(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]
        dispatcher.utter_message("Let's start over.")
        return [Restarted()]
