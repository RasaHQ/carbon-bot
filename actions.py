# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
from math import sin, cos, atan2, ceil, sqrt
from typing import Any, Text, Dict, List, Union, Optional
import logging
import re
import requests
import csv

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, Restarted
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase


logger = logging.getLogger(__name__)

URL_FLIGHT_EMISSION = "https://test-api.atmosfair.de/api/emission/flight"


def hyperlink_payload(tracker, message, title, url):
    return {
      "attachment":{
        "type":"template",
        "payload":{
          "template_type":"button",
          "text": message,
          "buttons":[
            {
              "type":"web_url",
              "url": url,
              "title": title,
              "webview_height_ratio": "full"
            }
          ]
        }
      }
    }


class AirportsKnowledgeBase(InMemoryKnowledgeBase):

    def load(self):
        def is_active(airport):
            return airport["type"].endswith("_airport") and \
                airport["scheduled_service"] == "yes"

        self.data = {"airport": []}
        with open(self.data_file, "r", encoding='utf-8') as f:

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
                lambda obj: obj["municipality"].lower() == city or \
                            city == obj["iata_code"].lower(),
                objects
            )
        )
        # sort airports by size
        sizes = [
            'large_airport',
            'medium_airport',
            'small_airport',
            'closed']
        objects = sorted(objects, key=lambda a: sizes.index(a['type']))

        # put US airports first
        objects = list(
            filter(
                lambda obj: obj["iso_country"] == "US",
                objects
            )
        ) + list(
            filter(
                lambda obj: obj["iso_country"] != "US",
                objects
            )
        )
        return objects

    @staticmethod
    def flight_class_code(code):
        codes = {
            "economy": "Y",
            "premium": "W",
            "business": "B",
            "first": "F"
        }
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
                "first": 1.30
            }.get(flight_class)
        else:
            # This does not include RFI
            co2_kg_per_km = {
                "economy": 0.18,
                "premium": 0.23,
                "business": 0.33,
                "first": 0.44
            }.get(flight_class)

        if not co2_kg_per_km:
            raise ValueError("Invalid flight class")

        return co2_kg_per_km * distance_km

    @staticmethod
    def co2_kg_atmosfair(departure_iata, destination_iata, flight_class):
        payload = {
            "username": "kundentest",
            "password": "kundentest",
            "flights":
                [
                    {
                        "departure": departure_iata,
                        "arrival": destination_iata,
                        "passengerCount": 1,
                        "travelClass": AirportsKnowledgeBase.flight_class_code(flight_class)
                    }
                ]
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

        a = sin(delta_phi * 0.5) * sin(delta_phi * 0.5) \
            + cos(phi_1) * cos(phi_2) * sin(delta_lam * 0.5) * sin(delta_lam * 0.5)
        c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
        return ceil(r * c / 100.) * 100

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
            raise ValueError(f"Could not find departure airport with IATA code '{departure_iata}'")
        if not destination_airport:
            raise ValueError(f"Could not find destination airport with IATA code '{departure_iata}'")

        # Compute the great circle distance between the two airports
        lat_a = departure_airport["latitude_deg"]
        lon_a = departure_airport["longitude_deg"]
        lat_b = destination_airport["latitude_deg"]
        lon_b = destination_airport["longitude_deg"]
        distance_km = self.great_circle_distance_km(lat_a, lon_a, lat_b, lon_b)

        co2_kg = self.co2_kg_interpolation(distance_km, flight_class)

        if not co2_kg:
            raise ValueError("CO2 amount could not be calculated.")

        kilos_per_unit = {
            "kilograms": 1.,
            "short_tons": 907.,    # Used in the US
            "long_tons": 1016.,    # Used in UK and Commonwealth
            "metric_tons": 1000.,  # Used by sensible people
        }.get(unit)

        if not kilos_per_unit:
            raise ValueError(f"Unknown unit: '{unit}'")

        unit_string = "kg" if unit == "kilograms" else "tons"

        co2 = f"{ceil(10 * co2_kg / kilos_per_unit) * 0.1:.1f} {unit_string}"
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
              f"&destination=https://offset.climateneutralnow.org/allprojects"

        link_1_url = url + f"&label=link-1-clicked"
        link_2_url = url + f"&label=link-2-clicked"

        return [SlotSet("link_1_url", link_1_url), SlotSet("link_2_url", link_2_url)]


AIRPORT_KB = AirportsKnowledgeBase("data/airports.csv")


class AirTravelForm(FormAction):
    def __init__(self):
        self.kb = AIRPORT_KB
        super(AirTravelForm, self).__init__()

    def name(self) -> Text:
        return "airtravel_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["travel_flight_class", "travel_departure", "travel_destination"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "travel_departure": [
                self.from_trigger_intent("TRIGGER", intent="inform"),
                self.from_text(intent="inform"),
            ],
            "travel_destination": [
                self.from_trigger_intent("TRIGGER", intent="inform"),
                self.from_text(intent="inform"),
            ],
            "travel_flight_class": [
                self.from_intent(intent="affirm", value="economy"),
                self.from_intent(intent="deny", value="business"),
                self.from_entity("travel_flight_class")
            ],
        }

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
            result = {f"travel_{kind}": candidates[0]["name"],
                      f"iata_{kind}": candidates[0]["iata_code"]}
        else:
            result = {f"travel_{kind}": None,
                      f"iata_{kind}": None}
        return result

    @staticmethod
    def _pop_next_item(items: List[Text], key: Text) -> Optional[Text]:
        """
        Returns items[i + 1], where i is the index of key, and
        deletes items[i] and items[i + 1] from `items`.
        :param items: List of things
        :param key: Item left of the item of interest
        :return: items[i + 1] or None
        """
        try:
            i = items.index(key)
        except ValueError:
            return None
        if i < len(items) - 1:
            next_key = items[i + 1]
            items.remove(key)
            items.remove(next_key)
            return next_key
        else:
            items.remove(key)
            return None

    @staticmethod
    def explain_travel_plan(plan, dispatcher):
        explanation = None
        if plan.get("travel_departure") and plan.get("travel_destination"):
            explanation = f"Ok, so you'll be flying from {plan['travel_departure']} to {plan['travel_destination']}."
        elif plan.get("travel_departure"):
            explanation = f"So you'll be flying from {plan['travel_departure']}."
        elif plan.get("travel_destination"):
            explanation = f"So you'll be flying to {plan['travel_destination']}."

        dispatcher.utter_message(explanation)

    def analyze_travel_plan(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            expected: Optional[Text]
    ):
        # Set the slots that we expect to `None` for now
        # The user might provide the destination despite being asked for the
        # departure, or vice versa
        result = {}
        if not expected or expected == "departure":
            result.update({"travel_departure": None, "iata_departure": None})
        if not expected or expected == "destination":
            result.update({"travel_destination": None, "iata_destination": None})
        # Store current belief about departure and destination
        old_departure = (tracker.get_slot("travel_departure"), tracker.get_slot("iata_departure"))
        old_destination = (tracker.get_slot("travel_destination"), tracker.get_slot("iata_destination"))
        # The user may have entered multiple cities in one sentence
        msg = tracker.latest_message["text"]
        # Find all the cities that have been mentioned
        cities = [ent for ent in tracker.latest_message["entities"]
                  if ent["entity"] == "city"]
        # Find all IATA codes
        iatas = [ent for ent in tracker.latest_message["entities"]
                 if ent["entity"] == "iata"]

        # Create a list of "from", "to", and locations, such as
        # ["from", "TXL", "Singapore", "to", "Hong Kong"]
        match = re.search(r"\bfrom\b", msg, re.IGNORECASE)
        pos_from = match.start() if match else -1
        match = re.search(r"\bto\b", msg, re.IGNORECASE)
        pos_to = match.start() if match else -1
        keyword_positions = [(iata["value"], iata["start"]) for iata in iatas] + \
                            [(city["value"], city["start"]) for city in cities] + [
            ("from", pos_from),
            ("to", pos_to),
        ]
        keyword_positions.sort(key=lambda elem: elem[1])
        keywords = [kp[0] for kp in keyword_positions if kp[1] >= 0]

        # We expect the departure and destination locations to be the next keywords
        # after 'from' and 'to', respectively
        departure = self._pop_next_item(keywords, "from")
        destination = self._pop_next_item(keywords, "to")

        # Use remaining locations if departure or destination is still unknown
        if keywords:
            if not destination and (departure or expected != "departure"):
                destination = keywords[0]
            elif not departure and (destination or expected == "departure"):
                departure = keywords[0]

        # Fill `result` with all slots that we've learned
        for kind, value in [("departure", departure), ("destination", destination)]:
            result.update(
                self._location_to_slot_dict(
                    value, kind
                )
            )

        # If the departure or destination has changed,
        # explain the recognized flight plan to the user
        if (old_departure[0] and result.get("travel_departure") and
            (result.get("travel_departure"), result.get("iata_departure")) != old_departure) or \
           (old_destination[0] and result.get("travel_destination") and
            (result.get("travel_destination"), result.get("iata_destination")) != old_destination):
            self.explain_travel_plan(result, dispatcher)

        # Notify user that no airport was found
        if expected and not result.get(f"iata_{expected}"):
            # dispatcher.utter_template("utter_could_not_find_airport", tracker)
            if result.get(f"travel_{expected}") is not None:
                dispatcher.utter_message(
                    f"I couldn't find your {expected} airport in {result.get(f'travel_{expected}')}."
                )
            else:
                dispatcher.utter_message(
                    f"I'm not sure about your {expected} airport."
                )

        return result

    def validate_travel_departure(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
          ) -> Dict[Text, Any]:
        return self.analyze_travel_plan(
            dispatcher,
            tracker,
            None if value == "TRIGGER" else "departure"
        )

    def validate_travel_destination(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
          ) -> Dict[Text, Any]:
        return self.analyze_travel_plan(
            dispatcher,
            tracker,
            None if value == "TRIGGER" else "destination"
        )

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = tracker.get_slot("link_2_url")
        try:
            co2_in_tons = self.kb.calculate_emissions(tracker, unit="short_tons")
        except ValueError as e:
            logger.error(f"calculate_emissions failed with: {e}")
            dispatcher.utter_message("Sorry, I was unable to calculate that.")
            return []
        departure_airport = tracker.get_slot("travel_departure")
        departure_iata = tracker.get_slot("iata_departure")
        destination_airport = tracker.get_slot("travel_destination")
        destination_iata = tracker.get_slot("iata_destination")

        message = f"A one-way flight from {departure_airport} ({departure_iata}) to {destination_airport} ({destination_iata}) "\
                  f"emits {co2_in_tons} of CO2. " \
                  f"It would be amazing if you bought offsets for that carbon! " \
                  f"There are some great, UN-certified projects you can pick from."

        if tracker.get_latest_input_channel() == "facebook":
            payload = hyperlink_payload(tracker, message, "Buy Offsets", url)
            dispatcher.utter_custom_json(payload)
        else:
            dispatcher.utter_message(message + f" [Buy Offsets]({url})")
        return [
            SlotSet("travel_departure"),
            SlotSet("iata_departure"),
            SlotSet("travel_destination"),
            SlotSet("iata_destination"),
            SlotSet("travel_flight_class")
        ]


class ExplainTypicalEmissions(Action):

    def name(self):
        return "action_explain_typical_emissions"

    def run(self, dispatcher, tracker, domain):
        url = tracker.get_slot("link_1_url")
        message = "A typical 3 hour flight will emit almost a ton of CO2 per economy passenger. "\
                  "If you cannot avoid flying, you can buy offsets for that carbon here: "
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
        message = "Hello! Just a heads up - this bot is part of a research " \
           "project and we intend to make the conversations publicly available " \
           "to researchers. So please don't share any personal information!"

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
