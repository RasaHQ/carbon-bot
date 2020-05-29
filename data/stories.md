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
    - form{"name":"airtravel_form"}


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
    - form{"name":"airtravel_form"}


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
    - form{"name":"airtravel_form"}

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


## 
    - submit_airtravel_form
    - form{"name": null}
    - slot{"requested_slot": null}
* faq
    - respond_faq
* thank
    - utter_express_positive-emo
    - utter_farewell