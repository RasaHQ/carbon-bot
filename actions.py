# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
from math import sin, cos, atan2, ceil, sqrt
from typing import Any, Text, Dict, List, Union, Optional, Tuple
import logging
import re
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
        stopover_iata = tracker.get_slot("iata_stopover")

        if not departure_iata:
            raise ValueError("Departure IATA code unknown.")
        if not destination_iata:
            raise ValueError("Destination IATA code unknown.")
        if not flight_class:
            raise ValueError("Flight class unknown.")

        departure_airport = self.find_airport_by_ref(departure_iata)
        destination_airport = self.find_airport_by_ref(destination_iata)
        if stopover_iata:
            stopover_airport = self.find_airport_by_ref(stopover_iata)
            if not stopover_airport:
                raise ValueError(
                    f"Could not find stopover airport with IATA code '{stopover_iata}'"
                )
            lat_stopover = stopover_airport["latitude_deg"]
            lon_stopover = stopover_airport["longitude_deg"]

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

        if stopover_iata:
            distance_km_leg1 = self.great_circle_distance_km(
                lat_a, lon_a, lat_stopover, lon_stopover
            )
            distance_km_leg2 = self.great_circle_distance_km(
                lat_stopover, lon_stopover, lat_b, lon_b
            )

        co2_kg = self.co2_kg_interpolation(distance_km, flight_class)
        if not co2_kg:
            raise ValueError("CO2 amount could not be calculated.")
        if stopover_iata:
            co2_kg_leg1 = self.co2_kg_interpolation(distance_km_leg1, flight_class)
            co2_kg_leg2 = self.co2_kg_interpolation(distance_km_leg2, flight_class)
            if not co2_kg_leg2 or not co2_kg_leg1:
                raise ValueError(
                    "CO2 amount could not be calculated for one of the legs."
                )

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
        if stopover_iata:
            co2_leg1 = (
                f"{ceil(10 * co2_kg_leg1 / kilos_per_unit) * 0.1:.1f} {unit_string}"
            )
            co2_leg2 = (
                f"{ceil(10 * co2_kg_leg2 / kilos_per_unit) * 0.1:.1f} {unit_string}"
            )
            co2 = (co2_leg1, co2_leg2)
        return co2


ordinal_mention_mapping = {
    "1": lambda l: l[0],
    "2": lambda l: l[1],
    "3": lambda l: l[2],
    "LAST": lambda l: l[-1],
}


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

        url = f"https://rasa.com/carbon/index.html?" \
              f"&rasaxhost=https://carbon.rasa.com" \
              f"&conversationId={tracker.sender_id}" \
              f"&destination=https://offset.earth%2F%3Fr%3D5de3ac5d7e813f00184649ea"

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

    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[List[Text]]:

        return [
            "travel_flight_class", 
            "travel_departure", 
            "travel_destination",
        ]

#    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#        return {
#            "travel_departure": [
#                self.from_entity(entity="city", role="from"),
#                self.from_entity(entity="iata", role="from"),
#                self.from_entity(entity="city"),
#                self.from_entity(entity="iata"),
#                self.from_text(intent="inform"),
#            ],
#            "travel_destination": [
#                self.from_entity(entity="city", role="to"),
#                self.from_entity(entity="iata", role="to"),
#                self.from_entity(entity="city"),
#                self.from_entity(entity="iata"),
#                self.from_text(intent="inform"),
#            ],
#            "previous_entered_flight": [
#                self.from_text(intent="inform"),
#            ],
#            "travel_flight_class": [
#                self.from_intent(intent="affirm", value="economy"),
#                self.from_intent(intent="deny", value="business"),
#                self.from_entity("travel_flight_class"),
#            ],
#        }
#
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

    def check_stopover(
        self,
        old_departure: Tuple,
        old_destination: Tuple,
        current_result: Dict,
        tracker: Tracker,
    ) -> Tuple[bool, Tuple]:
        """
        Checks whether the most recent trip is a connecting flight with the previous one;

        Args: 
            old_departure: (departure airport name, departure IATA code) tuple with departure airport
            entered within this form
            old destination: (destination airport name, destination IATA code) tuple with destination airport
            entered within this form
            current_result: dictionary with slot values provided in the last utterance
            tracker: state tracker containing current dialog state

        Returns: 
            second_leg_provided: a boolean flag of whether a connecting flight was found;
            stopover_tuple: if it was found:
                                a tuple of ((departure airport name, departure IATA code), (stopover airport name, stopover IATA code), 
                                (destination airport name, destination IATA code))
         
        """
        stopover_info = collections.namedtuple('Stopover_Info', ['second_leg_provided', 'stopover_tuple'])
        departure, destination, stopover = (None, None), (None, None), (None, None)

        if tracker.get_slot("previous_entered_flight")[1][0] in [
            old_departure[0],
            current_result.get("travel_departure"),
        ]:
            departure = tracker.get_slot("previous_entered_flight")[0]
            stopover = tracker.get_slot("previous_entered_flight")[1]
            if current_result.get("travel_destination"):
                destination = (
                    current_result["travel_destination"],
                    current_result["iata_destination"],
                )
            elif old_destination:
                destination = old_destination
        elif tracker.get_slot("previous_entered_flight")[0][0] in [
            old_destination[0],
            current_result.get("travel_destination"),
        ]:
            destination = tracker.get_slot("previous_entered_flight")[1]
            stopover = tracker.get_slot("previous_entered_flight")[0]
            if current_result.get("travel_departure"):
                departure = (
                    current_result["travel_departure"],
                    current_result["iata_departure"],
                )
            elif old_departure:
                departure = old_departure

        return stopover_info(
            second_leg_provided = None not in (departure[0], destination[0], stopover[0]),
            stopover_tuple = (departure, stopover, destination),
        )

    def departure_changed(self, old_departure, result):
        # checks that there is a new departure and it is not the same as old one;
        departure_change = (
            old_departure[0]
            and result.get("travel_departure")
            and (result.get("travel_departure"), result.get("iata_departure"))
            != old_departure
        )
        return departure_change

    def destination_changed(self, old_destination, result):
        destination_change = (
            old_destination[0]
            and result.get("travel_destination")
            and (result.get("travel_destination"), result.get("iata_destination"))
            != old_destination
        )
        return destination_change



class CalculateOffsets(Action):
    """Attempts to calculate CO2 usage and display link to purchase offsets."""

    def name(self) -> Text:
        return "action_calculate_offsets"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> List[Dict[Text, Any]]:

        url = tracker.get_slot("link_2_url")
        try:
            co2_in_tons = AIRPORT_KB.calculate_emissions(
                tracker, 
                unit="short_tons"
            )

        except ValueError as e:
            logger.error(f"calculate_emissions failed with: {e}")
            dispatcher.utter_message("Sorry, I was unable to calculate that.")
            return []

        departure_airport = tracker.get_slot("travel_departure")
        departure_iata = tracker.get_slot("iata_departure")
        destination_airport = tracker.get_slot("travel_destination")
        destination_iata = tracker.get_slot("iata_destination")
#        stopover_airport = tracker.get_slot("travel_stopover")
#        stopover_iata = tracker.get_slot("iata_stopover")
#        previous_entered_flight = tracker.get_slot("previous_entered_flight")
#
#        if not stopover_iata:
        if True:
            message = (
                f"A one-way flight from {departure_airport} ({departure_iata}) to {destination_airport} ({destination_iata}) "
                f"emits {co2_in_tons[0]} of CO2. "
                f"It would be amazing if you bought offsets for that carbon! "
                f"There are some great, UN-certified projects you can pick from."
            )
#        else:
#            message = (
#                f"The trip from {departure_airport} ({departure_iata}) to {destination_airport} ({destination_iata}) "
#                f"via {stopover_airport} ({stopover_iata}) emits {float(co2_in_tons[0].split()[0])+float(co2_in_tons[1].split()[0]):.1f} {co2_in_tons[0].split()[1]} of CO2. "
#                f"The first leg emits {co2_in_tons[0]} of CO2. "
#                f"The second leg emits {co2_in_tons[1]} of CO2."
#                f"It would be amazing if you bought offsets for that carbon! "
#                f"There are some great, UN-certified projects you can pick from."
#            )
#
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
            SlotSet("travel_stopover"),
            SlotSet("iata_stopover"),
            SlotSet("travel_flight_class"),
        ]

#        if tracker.get_slot("travel_stopover"):
#            return slots_to_set + [
#                SlotSet("previous_entered_flight"),
#            ]
#        else:
#            return slots_to_set
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
