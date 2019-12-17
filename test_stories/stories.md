## SCENARIO CHECK
* greet: hello
  - utter_SCENARIOCHECK

## faq
* faq: wassup
  - respond_faq
* thank: thanks
  - utter_express_positive-emo
* faq: wassup
  - respond_faq

## Story from conversation with b59c8f85-caea-4143-bae0-62421e93b664 on October 27th 2019
* greet: hello
    - utter_SCENARIOCHECK
* SCENARIO: /SCENARIO{"context_scenario":"holiday","holiday_name":"thanksgiving"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - action_start
    - slot{"link_1_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=b59c8f85-caea-4143-bae0-62421e93b664&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url":"https://rasa.com/carbon/index.html?&rasaxhost=http://localhost:5002&conversationId=b59c8f85-caea-4143-bae0-62421e93b664&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* why: why should I?
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"thanksgiving"}
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm: ok
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* affirm: ok
    - airtravel_form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
* why: why?
    - utter_explain_economy_class
    - airtravel_form
    - slot{"requested_slot":"travel_flight_class"}
* affirm: yes
    - airtravel_form
    - slot{"travel_flight_class":"economy"}
    - slot{"requested_slot":"travel_departure"}
* inform{"city": "Seattle"}: Seattle
    - airtravel_form
    - slot{"travel_departure":"Seattle"}
    - slot{"requested_slot":"travel_destination"}
* inform{"city":"Grand Rapids"}: Grand Rapids
    - slot{"city":"Grand Rapids"}
    - airtravel_form
    - slot{"travel_destination":"Grand Rapids"}
    - form{"name":null}
    - slot{"requested_slot":null}
* express_surprise: wow!
    - utter_explain_offset_calculation
* thank: thanks
    - utter_express_positive-emo
    - utter_farewell

## interactive_story_1
* greet: hello
    - utter_SCENARIOCHECK
* SCENARIO: /SCENARIO{"context_scenario": "holiday", "holiday_name": "christmas"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "christmas"}
    - action_start
    - slot{"link_1_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=3bc0234bd09447aaaaaa9beafa9550f3&destination=https://offset.climateneutralnow.org/allprojects&label=link-1-clicked"}
    - slot{"link_2_url": "https://rasa.com/carbon/index.html?&rasaxhost=https://carbon.rasa.com&conversationId=3bc0234bd09447aaaaaa9beafa9550f3&destination=https://offset.climateneutralnow.org/allprojects&label=link-2-clicked"}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* affirm: yes
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate
* affirm: yea
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm: yes
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - slot{"requested_slot": "travel_departure"}
* form: inform{"city": "Auckland"}: Auckland
    - slot{"city": ["Auckland"]}
    - form: airtravel_form
    - slot{"travel_departure": "Auckland International Airport"}
    - slot{"iata_departure": "AKL"}
    - slot{"requested_slot": "travel_destination"}
* form: inform{"city": "Glasgow"}: Glasgow
    - slot{"city": ["Glasgow"]}
    - form: airtravel_form
    - slot{"travel_destination": "Wokal Field Glasgow International Airport"}
    - slot{"iata_destination": "GGW"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thank: thanks
    - utter_express_positive-emo
    - utter_farewell

## filling travel plan before airtravel_form
* SCENARIO: /SCENARIO{"context_scenario": "holiday", "holiday_name": "thanksgiving"}
    - slot{"context_scenario": "holiday"}
    - slot{"holiday_name": "thanksgiving"}
    - action_start
    - slot{"link_1_url": "..."}
    - slot{"link_2_url": "..."}
    - action_disclaimer
    - utter_holiday-travel_offer_help
* inform{"city": ["berlin", "Madrid"]}: I'm going from Berlin to Madrid
    - slot{"city": ["berlin", "Madrid"]}
    - airtravel_form
    - form{"name": "airtravel_form"}
    - slot{"travel_departure": "Berlin-Schönefeld Airport"}
    - slot{"travel_destination": "Adolfo Suárez Madrid–Barajas Airport"}
    - slot{"iata_departure": "SXF"}
    - slot{"iata_destination": "MAD"}
    - slot{"requested_slot": "travel_flight_class"}
* form: affirm: yes
    - form: airtravel_form
    - slot{"travel_flight_class": "economy"}
    - form{"name": null}
    - slot{"requested_slot": null}
