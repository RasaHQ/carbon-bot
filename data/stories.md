## SCENARIO CHECK
* greet
  - utter_SCENARIOCHECK

## faqs
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* thank
  - utter_express_positive-emo
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* affirm
  - utter_acknowledge
* faq
  - respond_faq
* affirm
  - utter_acknowledge
* faq
  - respond_faq
* thank
  - utter_express_positive-emo
* faq
  - respond_faq

## give_travel_plan (1)
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* inform
    - airtravel_form
    - form{"name": "airtravel_form"}
    - form{"name": null}

## give_travel_plan (2)
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* inform
    - airtravel_form
    - form{"name": "airtravel_form"}
    - form{"name": null}

## interactive_story_1
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - form{"name": null}
* thank
    - utter_express_positive-emo
    - utter_farewell

## interactive_story_2
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* inform{"city": "Berlin"}
    - airtravel_form
    - form{"name": "airtravel_form"}
    - form{"name": null}
* thank
    - utter_express_positive-emo
    - utter_farewell

## interactive_story_3
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* deny
    - utter_acknowledge
    - action_explain_typical_emissions

## interactive_story_4
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* deny_flying
    - utter_acknowledge
    - action_explain_typical_emissions

## manual_story_1
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - utter_ask_detailed_estimate
* inform
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform{"city": "vancouver"}
    - airtravel_form
    - slot{"travel_departure":"London"}
    - slot{"requested_slot":"travel_destination"}
* inform
    - airtravel_form
    - slot{"travel_destination":"Berlin"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"city": "vancouver"}
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform{"city": "berlin"}
    - airtravel_form
    - slot{"travel_departure":"London"}
    - slot{"requested_slot":"travel_destination"}
* inform{"city": "seattle"}
    - airtravel_form
    - slot{"travel_destination":"Berlin"}
    - form{"name":null}
    - slot{"requested_slot":null}

## manual_story_2
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - utter_ask_detailed_estimate
* inform{"city": "seattle"}
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
    - slot{"context_scenario":"holiday"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - slot{"holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
* affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform
    - airtravel_form
    - slot{"travel_departure":"London"}
    - slot{"requested_slot":"travel_destination"}
* inform
    - airtravel_form
    - slot{"travel_destination":"Bearskin Lake"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"city": "seattle"}
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform{"city": "Paris"}
    - airtravel_form
    - slot{"travel_departure":"London"}
    - slot{"requested_slot":"travel_destination"}
* inform
    - airtravel_form
    - slot{"travel_destination":"Bearskin Lake"}
    - form{"name":null}
    - slot{"requested_slot":null}

## interactive_story_6
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* why
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}

## Story from conversation with 14e4c5ba-abba-4be1-8b22-e6e4f2fd2508 on October 26th 2019
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=14e4c5ba-abba-4be1-8b22-e6e4f2fd2508&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=14e4c5ba-abba-4be1-8b22-e6e4f2fd2508&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_explain_typical_emissions
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - utter_ask_detailed_estimate
* inform{"city":"Berlin"}
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform{"city":"Berlin"}
    - airtravel_form
    - slot{"travel_departure":"Berlin"}
    - slot{"requested_slot":"travel_destination"}
* inform
    - airtravel_form
    - slot{"travel_destination":"Dublin"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"city": "new york"}
    - airtravel_form
    - slot{"travel_destination":"Dublin"}
    - form{"name":null}
    - slot{"requested_slot":null}
* express_surprise
    - utter_explain_offset_calculation

## Story from conversation with 35ebdd5a-34a3-4707-89f2-4748c4997620 on October 27th 2019
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
* greet
    - utter_greet
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* inform
    - airtravel_form

## Story from conversation with b59c8f85-caea-4143-bae0-62421e93b664 on October 27th 2019
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=b59c8f85-caea-4143-bae0-62421e93b664&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=b59c8f85-caea-4143-bae0-62421e93b664&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* why
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* why
    - utter_explain_economy_class
    - airtravel_form
    - slot{"requested_slot":"travel_flight_class"}
* affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform
    - airtravel_form
    - slot{"travel_departure":"Seattle"}
    - slot{"requested_slot":"travel_destination"}
* inform{"city":"Grand Rapids"}
    - airtravel_form
    - slot{"travel_destination":"Grand Rapids"}
    - form{"name":null}
    - slot{"requested_slot":null}
* express_surprise
    - utter_explain_offset_calculation
* thank
    - utter_express_positive-emo
    - utter_farewell

## manual_story_3
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=b1efba67bc4c44f0b0b25b07d56e62aa&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=b1efba67bc4c44f0b0b25b07d56e62aa&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
* inquire-ask_clarification-offsets
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* faq
    - respond_faq
* faq
    - respond_faq
* affirm
    - utter_acknowledge
* farewell
    - utter_farewell

## manual_story_4
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=6262c031c02b4c50b1be929b9f25465f&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=6262c031c02b4c50b1be929b9f25465f&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
* greet
    - utter_greet
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - form{"name": null}
* thank
    - utter_express_positive-emo
    - utter_farewell

## interactive_story_7
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=cd2e1e21b3c0495784b155be697da14c&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=cd2e1e21b3c0495784b155be697da14c&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"requested_slot": "travel_departure"}
* form: affirm{"iata": "SFO"}
    - form: airtravel_form
    - slot{"travel_departure": "San Francisco International Airport"}
    - slot{"iata_departure": "SFO"}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"iata": "SAD"}
    - form: airtravel_form
    - slot{"travel_destination": null}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"iata": "SAD"}
    - form: airtravel_form
    - slot{"travel_destination": null}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"city": "San Diego"}
    - form: airtravel_form
    - slot{"travel_destination": "San Diego International Airport"}
    - slot{"iata_destination": "SAN"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_express_positive-emo
    - utter_farewell

## interactive_story_8
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=26cbf7ec501f41408ca682834c9c6f3c&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=26cbf7ec501f41408ca682834c9c6f3c&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}
* form: inform{"city": "boston"}
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"requested_slot": "travel_departure"}
* form: inform{"city": "Los Angeles"}
    - form: airtravel_form
    - slot{"travel_departure": "Los Angeles International Airport"}
    - slot{"iata_departure": "LAX"}
    - slot{"requested_slot": "travel_destination"}
* faq
    - respond_faq
    - airtravel_form
    - slot{"requested_slot": "travel_destination"}
* form: inform{"city": "Pittsburgh"}
    - form: airtravel_form
    - slot{"travel_destination": "Pittsburgh International Airport"}
    - slot{"iata_destination": "PIT"}
    - form{"name": null}
    - slot{"requested_slot": null}
* faq
    - respond_faq
* faq
    - respond_faq

## interactive_story_9
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=26cbf7ec501f41408ca682834c9c6f3c&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=26cbf7ec501f41408ca682834c9c6f3c&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* faq
    - respond_faq
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}
* form: inform{"city": "boston"}
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"requested_slot": "travel_departure"}
* form: inform{"city": "Los Angeles"}
    - form: airtravel_form
    - slot{"travel_departure": "Los Angeles International Airport"}
    - slot{"iata_departure": "LAX"}
    - slot{"requested_slot": "travel_destination"}
* faq
    - respond_faq
* faq
    - respond_faq
    - airtravel_form
    - slot{"requested_slot": "travel_destination"}
* form: inform{"city": "Pittsburgh"}
    - form: airtravel_form
    - slot{"travel_destination": "Pittsburgh International Airport"}
    - slot{"iata_destination": "PIT"}
    - form{"name": null}
    - slot{"requested_slot": null}
* faq
    - respond_faq
* faq
    - respond_faq

## interactive_story_10
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=d3d8ffc8f70c4fed9b4827c4b1ccdb61&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=d3d8ffc8f70c4fed9b4827c4b1ccdb61&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* why
    - utter_explain_economy_class
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"requested_slot": "travel_departure"}
* form: inform{"city": "Detroit"}
    - form: airtravel_form
    - slot{"travel_departure": "Detroit Metropolitan Wayne County Airport"}
    - slot{"iata_departure": "DTW"}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"iata": "DFW"}
    - form: airtravel_form
    - slot{"travel_destination": "Dallas Fort Worth International Airport"}
    - slot{"iata_destination": "DFW"}
    - form{"name": null}
    - slot{"requested_slot": null}
* faq
    - respond_faq
* faq
    - respond_faq
* affirm
    - utter_acknowledge
* thank
    - utter_express_positive-emo
* farewell
    - utter_farewell

## interactive_story_11
* affirm
    - utter_acknowledge
* faq
    - respond_faq
* affirm
    - utter_acknowledge
* faq
    - respond_faq
* why
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
* affirm
    - utter_acknowledge
* inform{"city": "Boston"}
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"requested_slot": "travel_departure"}
* form: inform{"city": "Austin"}
    - form: airtravel_form
    - slot{"travel_departure": "Austin Bergstrom International Airport"}
    - slot{"iata_departure": "AUS"}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"city": "Boston"}
    - form: airtravel_form

## interactive_story_12
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=702b1366f10a451785e596acaac9a8f8&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=702b1366f10a451785e596acaac9a8f8&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* inquire-ask_clarification
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* express_uncertainty
    - utter_explain_how_offsets_work
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}

## interactive_story_13
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=cd770cc225544c7583540b0879e99549&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=cd770cc225544c7583540b0879e99549&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* express_negative-emo
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* deny_flying
    - utter_acknowledge
* faq
    - respond_faq

## interactive_story_14
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=cd770cc225544c7583540b0879e99549&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=cd770cc225544c7583540b0879e99549&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* express_negative-emo
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* deny
    - utter_acknowledge
* faq
    - respond_faq

## interactive_story_15
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=df9f5f1fc9d943b98939a95e5cd6a842&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=df9f5f1fc9d943b98939a95e5cd6a842&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* faq
    - respond_faq
* affirm
    - utter_acknowledge
* buy_offsets
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}

## interactive_story_16
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=df9f5f1fc9d943b98939a95e5cd6a842&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=df9f5f1fc9d943b98939a95e5cd6a842&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* faq
    - respond_faq
* faq
    - respond_faq
* affirm
    - utter_acknowledge
* buy_offsets
    - airtravel_form

## interactive_story_17
* faq
    - respond_faq
* faq
    - respond_faq
* affirm
    - utter_acknowledge
* buy_offsets
    - airtravel_form

## interactive_story_18
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* deny
    - utter_acknowledge
* faq
    - respond_faq
* farewell
    - utter_acknowledge
    - utter_farewell

## interactive_story_19
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* inquire-ask_clarification-offsets
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* express_uncertainty
    - utter_explain_how_offsets_work
* deny
    - utter_acknowledge
* faq
    - respond_faq
* buy_offsets
    - airtravel_form

## interactive_story_20
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* inquire-ask_clarification-offsets
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* express_surprise
    - utter_explain_how_offsets_work
* deny
    - utter_acknowledge
* faq
    - respond_faq
* buy_offsets
    - airtravel_form

## interactive_story_21
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=600e3f9b7dfc48ca93fb1edd68a5f388&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=600e3f9b7dfc48ca93fb1edd68a5f388&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* deny
    - utter_acknowledge

## Story from conversation with 14e4c5ba-abba-4be1-8b22-e6e4f2fd2508 on October 26th 2019 (1)
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=14e4c5ba-abba-4be1-8b22-e6e4f2fd2508&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=14e4c5ba-abba-4be1-8b22-e6e4f2fd2508&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_explain_typical_emissions
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - utter_ask_detailed_estimate
* inform{"city":"Berlin"}
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform{"city":"Berlin"}
    - airtravel_form
    - slot{"travel_departure":"Berlin"}
    - slot{"requested_slot":"travel_destination"}
* inform
    - airtravel_form
    - slot{"travel_destination":"Dublin"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform
    - airtravel_form
    - slot{"travel_destination":"Dublin"}
    - form{"name":null}
    - slot{"requested_slot":null}
* how_calculated
    - utter_explain_offset_calculation

## interactive_story_22
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "christmas"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "christmas"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help

## interactive_story_23
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "christmas"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "christmas"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=2968ccfd4e814f8b976094787c922319&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=2968ccfd4e814f8b976094787c922319&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"requested_slot": "travel_departure"}
* form: inform{"city": "Berlin"}
    - form: airtravel_form
    - slot{"travel_departure": "Berlin-Schönefeld Airport"}
    - slot{"iata_departure": "SXF"}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"city": "new york"}
    - form: airtravel_form
    - slot{"travel_destination": "John F Kennedy International Airport"}
    - slot{"iata_destination": "JFK"}
    - slot{"travel_departure": null}
    - slot{"iata_departure": null}
    - slot{"travel_destination": null}
    - slot{"iata_destination": null}
    - slot{"travel_flight_class": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* inform{"city": "vancouver"}
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"travel_departure": "London Airport"}
    - slot{"travel_destination": "Vancouver International Airport"}
    - slot{"iata_departure": "YXU"}
    - slot{"iata_destination": "YVR"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"travel_departure": null}
    - slot{"iata_departure": null}
    - slot{"travel_destination": null}
    - slot{"iata_destination": null}
    - slot{"travel_flight_class": null}
    - form{"name": null}
    - slot{"requested_slot": null}

## manual_story_5
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - utter_ask_detailed_estimate
* inform{"city": "seattle"}
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
    - slot{"context_scenario":"holiday"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - slot{"holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
* affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform
    - airtravel_form
    - slot{"travel_departure":"London"}
    - slot{"requested_slot":"travel_destination"}
* inform
    - airtravel_form
    - slot{"travel_destination":"Bearskin Lake"}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"city": "seattle"}
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform{"city": "Paris"}
    - airtravel_form
    - slot{"travel_departure":"London"}
    - slot{"requested_slot":"travel_destination"}
* inform
    - airtravel_form
    - slot{"travel_destination":"Bearskin Lake"}
    - form{"name":null}
    - slot{"requested_slot":null}
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* thank
  - utter_express_positive-emo

## interactive_story_24
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "christmas"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "christmas"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=a4fa38ac948c475b8505152b36d944d6&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=a4fa38ac948c475b8505152b36d944d6&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* inquire-ask_clarification-offsets
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* inquire-ask_clarification-offsets
    - utter_explain_how_offsets_work
    - utter_ask_detailed_estimate

## interactive_story_25
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=df9f5f1fc9d943b98939a95e5cd6a842&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=df9f5f1fc9d943b98939a95e5cd6a842&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* faq
    - respond_faq
* affirm
    - utter_acknowledge
* estimate_emissions
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}

## interactive_story_26
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=df9f5f1fc9d943b98939a95e5cd6a842&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=df9f5f1fc9d943b98939a95e5cd6a842&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* faq
    - respond_faq
* faq
    - respond_faq
* affirm
    - utter_acknowledge
* estimate_emissions
    - airtravel_form

## interactive_story_27
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - form{"name": null}
* buy_offsets
    - utter_explain_no_payment
* thank
    - utter_express_positive-emo
    - utter_farewell

## interactive_story_28
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=cd2e1e21b3c0495784b155be697da14c&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=cd2e1e21b3c0495784b155be697da14c&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"requested_slot": "travel_departure"}
* form: affirm{"iata": "SFO"}
    - form: airtravel_form
    - slot{"travel_departure": "San Francisco International Airport"}
    - slot{"iata_departure": "SFO"}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"iata": "SAD"}
    - form: airtravel_form
    - slot{"travel_destination": null}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"iata": "SAD"}
    - form: airtravel_form
    - slot{"travel_destination": null}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"city": "San Diego"}
    - form: airtravel_form
    - slot{"travel_destination": "San Diego International Airport"}
    - slot{"iata_destination": "SAN"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_express_positive-emo
    - utter_farewell
* buy_offsets
    - utter_explain_no_payment
* affirm
    - utter_acknowledge

## interactive_story_29
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "christmas"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "christmas"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=a237c6dccfe24422aa28a63e7dfed8f3&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=a237c6dccfe24422aa28a63e7dfed8f3&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"requested_slot": "travel_departure"}
* form: inform{"city": "Berlin"}
    - form: airtravel_form
    - slot{"travel_departure": "Berlin-Schönefeld Airport"}
    - slot{"iata_departure": "SXF"}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"city": "Paris"}
    - form: airtravel_form
    - slot{"travel_destination": "Charles de Gaulle International Airport"}
    - slot{"iata_destination": "CDG"}
    - slot{"travel_departure": null}
    - slot{"iata_departure": null}
    - slot{"travel_destination": null}
    - slot{"iata_destination": null}
    - slot{"travel_flight_class": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* inform{"city": "Seattle"}
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"travel_departure": "Charles de Gaulle International Airport"}
    - slot{"travel_destination": "Boeing Field King County International Airport"}
    - slot{"iata_departure": "CDG"}
    - slot{"iata_destination": "BFI"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"travel_departure": null}
    - slot{"iata_departure": null}
    - slot{"travel_destination": null}
    - slot{"iata_destination": null}
    - slot{"travel_flight_class": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_acknowledge
* inform{"city": "Dallas"}
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"travel_departure": "Boeing Field King County International Airport"}
    - slot{"travel_destination": "Dallas Love Field"}
    - slot{"iata_departure": "BFI"}
    - slot{"iata_destination": "DAL"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"travel_departure": null}
    - slot{"iata_departure": null}
    - slot{"travel_destination": null}
    - slot{"iata_destination": null}
    - slot{"travel_flight_class": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* faq
    - respond_faq
* thank
    - utter_express_positive-emo
    - utter_farewell

## interactive_story_30
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "christmas"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "christmas"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=21ed987a5d964c9999aeac98bc55efa3&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=21ed987a5d964c9999aeac98bc55efa3&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* inform{"city": "Chicago", "iata": "EWR"}
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"travel_departure": "Chicago Midway International Airport"}
    - slot{"travel_destination": "Newark Liberty International Airport"}
    - slot{"iata_departure": "MDW"}
    - slot{"iata_destination": "EWR"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"travel_departure": null}
    - slot{"iata_departure": null}
    - slot{"travel_destination": null}
    - slot{"iata_destination": null}
    - slot{"travel_flight_class": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* inform{"iata": "EWR"}
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"travel_departure": "Newark Liberty International Airport"}
    - slot{"travel_destination": null}
    - slot{"iata_departure": "EWR"}
    - slot{"iata_destination": null}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"city": "Chicago"}
    - form: airtravel_form
    - slot{"travel_destination": "Chicago Midway International Airport"}
    - slot{"iata_destination": "MDW"}
    - slot{"travel_departure": null}
    - slot{"iata_departure": null}
    - slot{"travel_destination": null}
    - slot{"iata_destination": null}
    - slot{"travel_flight_class": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* faq
    - respond_faq
* faq
    - respond_faq
* inform{"city": "Singapore"}
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"travel_departure": "John F Kennedy International Airport"}
    - slot{"travel_destination": "Singapore Changi Airport"}
    - slot{"iata_departure": "JFK"}
    - slot{"iata_destination": "SIN"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - form{"name": null}
    - slot{"requested_slot": null}
* faq
    - respond_faq
* thank
    - utter_express_positive-emo
    - utter_farewell

## interactive 33
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* inform_notunderstanding
  - utter_acknowledge_notunderstanding
* inform_notunderstanding
  - action_restart

## interactive 34
* faq
  - respond_faq
* faq
  - respond_faq
* faq
  - respond_faq
* inform_notunderstanding
  - utter_acknowledge_notunderstanding
* faq
  - respond_faq
* inform_notunderstanding
  - utter_acknowledge_notunderstanding
* faq
  - respond_faq

## interactive_story_35
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario": "holiday", "holiday_name": "christmas"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "christmas"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=c86e486da8614da8a1f338c465f3df51&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=c86e486da8614da8a1f338c465f3df51&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* inform_notunderstanding
    - utter_acknowledge_notunderstanding
* buy_offsets
    - airtravel_form

## Story from conversation with 2485257761521706 on December 1st 2019
* greet
    - utter_SCENARIOCHECK
* SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=2485257761521706&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=2485257761521706&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform{"city":"Los Angeles"}
    - airtravel_form
    - slot{"travel_departure":"Los Angeles International Airport"}
    - slot{"iata_departure":"LAX"}
    - slot{"requested_slot":"travel_destination"}
* inform{"city":"Chicago"}
    - airtravel_form
    - slot{"travel_destination":"Chicago Midway International Airport"}
    - slot{"iata_destination":"MDW"}
    - form{"name":null}
    - slot{"requested_slot":null}
* SCENARIO{"context_scenario":"holiday","holiday_name":"christmas"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"christmas"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=2485257761521706&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=2485257761521706&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* meta_inform_problem_bad-link
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"travel_flight_class":"economy"}
    - slot{"travel_departure":null}
    - slot{"travel_destination":null}
    - slot{"iata_departure":null}
    - slot{"iata_destination":null}
    - slot{"requested_slot":"travel_departure"}
* affirm
    - utter_acknowledge
* inform{"city":"Los Angeles"}
    - airtravel_form
    - slot{"travel_departure":"General Edward Lawrence Logan International Airport"}
    - slot{"iata_departure":"BOS"}
    - slot{"travel_destination":"Los Angeles International Airport"}
    - slot{"iata_destination":"LAX"}
    - slot{"travel_departure":null}
    - slot{"iata_departure":null}
    - slot{"travel_destination":null}
    - slot{"iata_destination":null}
    - slot{"travel_flight_class":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
* inquire-ask_clarification-offsets
    - utter_explain_how_offsets_work
* faq
    - respond_faq

## Story from conversation with 3afca642-97d5-4197-9252-a738c40604f1 on December 2nd 2019
* inform{"city":"new york","travel_flight_class":"economy"}
    - slot{"travel_flight_class":"economy"}
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"travel_flight_class":"economy"}
    - slot{"travel_flight_class":"economy"}
    - slot{"travel_departure":"General Edward Lawrence Logan International Airport"}
    - slot{"travel_destination":"John F Kennedy International Airport"}
    - slot{"iata_departure":"BOS"}
    - slot{"iata_destination":"JFK"}
    - slot{"travel_departure":null}
    - slot{"iata_departure":null}
    - slot{"travel_destination":null}
    - slot{"iata_destination":null}
    - slot{"travel_flight_class":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* inquire-ask_clarification-offsets
    - utter_explain_how_offsets_work
    - utter_ask_detailed_estimate
* inquire-ask_clarification-offsets
    - utter_explain_how_offsets_work
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* form: affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* form: inform{"city":"boston"}
    - airtravel_form
    - slot{"travel_departure":"General Edward Lawrence Logan International Airport"}
    - slot{"iata_departure":"BOS"}
    - slot{"requested_slot":"travel_destination"}
* form: inform{"city":"new york"}
    - airtravel_form
    - slot{"travel_destination":"John F Kennedy International Airport"}
    - slot{"iata_destination":"JFK"}
    - slot{"travel_departure":null}
    - slot{"iata_departure":null}
    - slot{"travel_destination":null}
    - slot{"iata_destination":null}
    - slot{"travel_flight_class":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* faq
    - respond_faq
* faq
    - respond_faq

## Story from conversation with 3259187940789816 on December 4th 2019

* SCENARIO{"context_scenario":"holiday","holiday_name":"christmas"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"christmas"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=3259187940789816&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=3259187940789816&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform{"city":"Austin"}
    - airtravel_form
    - slot{"travel_departure":"Austin Bergstrom International Airport"}
    - slot{"iata_departure":"AUS"}
    - slot{"requested_slot":"travel_destination"}
* inform{"city":"New York"}
    - airtravel_form
    - slot{"travel_destination":"John F Kennedy International Airport"}
    - slot{"iata_destination":"JFK"}
    - slot{"travel_departure":null}
    - slot{"iata_departure":null}
    - slot{"travel_destination":null}
    - slot{"iata_destination":null}
    - slot{"travel_flight_class":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"city":"Newark"}
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"travel_departure":null}
    - slot{"travel_destination":"Newark Liberty International Airport"}
    - slot{"iata_departure":null}
    - slot{"iata_destination":"EWR"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform{"city":"Austin"}
    - airtravel_form
    - slot{"travel_departure":"Austin Bergstrom International Airport"}
    - slot{"iata_departure":"AUS"}
    - slot{"travel_departure":null}
    - slot{"iata_departure":null}
    - slot{"travel_destination":null}
    - slot{"iata_destination":null}
    - slot{"travel_flight_class":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* express_positive-emo
    - utter_explain_offset_calculation
* express_positive-emo
    - utter_express_positive-emo

## Story from conversation with 2524603660920240 on December 12th 2019

* SCENARIO{"context_scenario":"holiday","holiday_name":"christmas"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"christmas"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=2524603660920240&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=2524603660920240&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* deny
    - utter_acknowledge
    - action_explain_typical_emissions
* why
    - utter_explain_why_offset_travel
    - utter_ask_detailed_estimate

## RUDE USER 1
* insult
    - utter_insult

## RUDE USER 2
* vulgar
    - utter_vulgar
