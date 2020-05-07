## SCENARIO CHECK
* greet
  - utter_SCENARIOCHECK

## faq
    - ...
* faq
  - respond_faq


## thank
    - ...
* thank
    - utter_express_positive-emo
    - ...


## greet
    - ...
* greet
    - utter_greet
    - ...


## not understand
    - ...
* inform_notunderstanding
    - utter_acknowledge_notunderstanding
  
## not understand restart
    - ...
* inform_notunderstanding
    - utter_acknowledge_notunderstanding
* inform_notunderstanding
    - action_restart


## scenario holiday
    - ...
* SCENARIO{"context_scenario":"holiday","holiday_name":"bla"}
    - slot{"context_scenario":"holiday"}
    - slot{"holiday_name":"bla"}
    - action_start
    - slot{"link_1_url":"some_url"}
    - slot{"link_2_url":"some_url"}
    - action_disclaimer
    - utter_holiday-travel_offer_help


## holiday affirm
    - ...
    - utter_holiday-travel_offer_help
* affirm
    - utter_explain_why_offset_travel
    - action_explain_typical_emissions
    - utter_ask_detailed_estimate


## deny
    - ...
    - utter_holiday-travel_offer_help
* deny OR deny_flying
    - utter_acknowledge
    - action_explain_typical_emissions


## start airtravel form
    - ...
    - utter_ask_detailed_estimate
* inform OR affirm
    - activate_airtravel_form
    - ...


## loop airtravel form
    - ...
    - activate_airtravel_form
    - form{"name":"airtravel_form"}
    - ask_travel_flight_class
    - slot{"requested_slot":"travel_flight_class"}
    
## loop airtravel form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_flight_class"}
    - ...
* affirm
    - validate_travel_flight_class
    - ask_travel_departure
    - slot{"requested_slot":"travel_departure"}

## loop airtravel form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_departure"}
    - ...
* inform
    - validate_travel_departure
    - ask_travel_destination
    - slot{"requested_slot":"travel_destination"}

## loop airtravel form
    - form{"name":"airtravel_form"}
    - slot{"requested_slot":"travel_destination"}
    - ...
* inform
    - validate_travel_destination
    - submit_airtravel_form
    - form{"name":null}
    - slot{"requested_slot":null}
    

## after form
    - ...
    - submit_airtravel_form
    - form{"name":null}
    - slot{"requested_slot":null}
* thank
    - utter_express_positive-emo
    - utter_farewell