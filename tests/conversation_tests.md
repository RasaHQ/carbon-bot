## Story from conversation with 2918155194886151 on April 21st 2020

* SCENARIO: /SCENARIO[holiday](context_sc[christmas](holiday_name)
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"christmas"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=2918155194886151&destination=https://offset.earth%2F%3Fr%3D5de3ac5d7e813f00184649ea&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=2918155194886151&destination=https://offset.earth%2F%3Fr%3D5de3ac5d7e813f00184649ea&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm: Yes
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm: Sure
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm: Yes
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform: [Bangalore](city)
    - slot{"city":["Bangalore"]}
    - airtravel_form
    - slot{"travel_departure":"Kempegowda International Airport"}
    - slot{"iata_departure":"BLR"}
    - slot{"requested_slot":"travel_destination"}
* inform: [San Francisco](city)
    - slot{"city":["San Francisco"]}
    - airtravel_form
    - slot{"travel_destination":"San Francisco International Airport"}
    - slot{"iata_destination":"SFO"}
    - slot{"travel_departure":null}
    - slot{"iata_departure":null}
    - slot{"travel_destination":null}
    - slot{"iata_destination":null}
    - slot{"travel_flight_class":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* why: Tell me more
    - utter_explain_economy_class
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm: Yes
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform: [Blr](iata)
    - airtravel_form
    - slot{"travel_departure":"Kempegowda International Airport"}
    - slot{"iata_departure":"BLR"}
    - slot{"requested_slot":"travel_destination"}
* inform: [Sfo](iata)
    - airtravel_form
    - slot{"travel_destination":"San Francisco International Airport"}
    - slot{"iata_destination":"SFO"}
    - slot{"travel_departure":null}
    - slot{"iata_departure":null}
    - slot{"travel_destination":null}
    - slot{"iata_destination":null}
    - slot{"travel_flight_class":null}
    - form{"name":null}
    - slot{"requested_slot":null}
