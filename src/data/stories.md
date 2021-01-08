## greet
* greet
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_how_can_i_help

## ask functions
* ask_functions
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_explain_functions

## ask repeat
* ask_repeat
    - action_repeat

## goodbye
* goodbye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## thanks and bye
* thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_you_are_welcome_ask_something_else
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## explain and preparation
* explain{"cocktail": "margarita"}
    - slot{"cocktail": "margarita"}
    - action_explain
    - slot{"cocktail": "margarita"}
* ask_preparation
    - action_preparation
    - slot{"cocktail": "margarita"}

## preparation
* ask_preparation{"cocktail": "negroni"}
    - slot{"cocktail": "negroni"}
    - action_preparation
    - slot{"cocktail": "negroni"}

## search 1 option
* search_provider
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - form: search_form
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider{"ingredient": "vodka"}
    - form: search_form
    - slot{"ingredient": ["vodka"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider{"ingredient": "rum"}
    - form: search_form
    - slot{"ingredient": ["gin"]}
    - slot{"multiple_options": true}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka,gin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider{"ingredient": "light rum"}
    - form: search_form
    - slot{"ingredient": ["light rum"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka,gin,light rum"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "vodka,gin,light rum"}
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka,gin,light rum"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "long island iced tea"}
    - utter_ask_explanation
* affirm
    - action_explain
    - slot{"cocktail": "long island iced tea"}
* ask_preparation
    - action_preparation
    - slot{"cocktail": "long island iced tea"}
* ask_repeat
    - action_repeat

## search more options explain
* search_provider{"category": "cocktail", "ingredient": "vodka"}
    - slot{"category": "cocktail"}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["vodka"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "vodka"}
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka"}
    - slot{"proposes": "espresso martini,dirty martini,bloody mary"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka"}
    - slot{"proposes": "espresso martini,dirty martini,bloody mary,french martini,vesper,harvey wallbanger"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* explain{"cocktail": "vesper"}
    - slot{"cocktail": "vesper"}
    - action_explain
    - slot{"cocktail": "vesper"}
    - action_continue
* deny
    - choice_form
    - form{"name": "choice_form"}
    - slot{"requested_slot": "cardinal"}
* form: cardinal{"cardinal": "3"}
    - slot{"cardinal": "3"}
    - choice_form
    - slot{"cardinal": 2}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "bloody mary"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation
* affirm
    - action_explain
    - slot{"cocktail": "bloody mary"}
* ask_repeat
    - action_repeat

## search more options choice explain 1
* search_provider{"ingredient": "gin"}
    - search_form
    - form{"name": "search_form"}
    - slot{"ingredient": ["gin"]}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "category"}
* form: search_provider{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - form: search_form
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "gin"}
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "gin"}
    - slot{"proposes": "tuxedo cocktail,martini,aviation"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* deny
    - choice_form
    - form{"name": "choice_form"}
    - slot{"requested_slot": "cardinal"}
* explain{"cocktail": "rose"}
    - slot{"cocktail": "rose"}
    - action_explain
    - slot{"cocktail": "rose"}
    - action_continue
    - action_listen
* form: cardinal{"cardinal": "1"}
    - slot{"cardinal": "1"}
    - choice_form
    - slot{"cardinal": 0}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "tuxedo cocktail"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_ask_something_else
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## search no confirm
* search_provider
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider{"ingredient": "vodka"}
    - form: search_form
    - slot{"ingredient": ["gin", "vodka"]}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "category"}
* form: search_provider{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - form: search_form
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin,vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "gin,vodka"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_ask_something_else
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## search 1 no explain
* search_provider{"category": "cocktail", "ingredient": "vodka"}
    - slot{"category": "cocktail"}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["gin", "vodka"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin,vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider{"ingredient": "light rum"}
    - form: search_form
    - slot{"ingredient": ["light rum"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin,vodka,light rum"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "gin,vodka,light rum"}
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "gin,vodka,light rum"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "long island iced tea"}
    - utter_ask_explanation
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_ask_something_else
* explain{"cocktail": "margarita"}
    - slot{"cocktail": "margarita"}
    - action_explain
    - slot{"cocktail": "margarita"}
* ask_preparation
    - action_preparation
    - slot{"cocktail": "margarita"}
* thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_you_are_welcome_ask_something_else
* ask_functions
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_explain_functions
    
## ask ingredients in search and continue
* search_provider{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider{"ingredient": "white rum"}
    - form: search_form
    - slot{"ingredient": ["gin", "white rum"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin,white rum"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* ask_ingredients
    - action_list_ingredients
    - slot{"ingr_list": "gin,white rum"}
    - utter_ask_continue
* affirm
    - search_form
    - slot{"requested_slot": "ingredient"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "gin,white rum"}
* affirm
    - action_search
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_ask_something_else
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## ask ingredients in search and stop
* search_provider{"category": "cocktail", "ingredient": "gin"}
    - slot{"category": "cocktail"}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["gin"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider{"ingredient": "tequila"}
    - form: search_form
    - slot{"ingredient": ["white rum", "tequila"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin,white rum,tequila"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* ask_ingredients
    - action_list_ingredients
    - slot{"ingr_list": "gin,white rum,tequila"}
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_ask_something_else
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## multiple explain in more options
* search_provider{"category": "cocktail", "ingredient": "vodka"}
    - slot{"category": "cocktail"}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["vodka"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "vodka"}
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka"}
    - slot{"proposes": "espresso martini,moscow mule,dirty martini"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* explain{"cocktail": "moscow mule"}
    - slot{"cocktail": "moscow mule"}
    - action_explain
    - slot{"cocktail": "moscow mule"}
    - action_continue
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka"}
    - slot{"proposes": "espresso martini,moscow mule,dirty martini,vesper,sea breeze,screwdriver"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* explain{"cocktail": "vesper"}
    - slot{"cocktail": "vesper"}
    - action_explain
    - slot{"cocktail": "vesper"}
    - action_continue
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka"}
    - slot{"proposes": "espresso martini,moscow mule,dirty martini,vesper,sea breeze,screwdriver,kamikaze,harvey wallbanger,french martini"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* explain{"cocktail": "kamikaze"}
    - slot{"cocktail": "kamikaze"}
    - action_explain
    - slot{"cocktail": "kamikaze"}
    - action_continue
* explain{"cocktail": "french martini"}
    - slot{"cocktail": "french martini"}
    - action_explain
    - slot{"cocktail": "french martini"}
    - action_continue
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka"}
    - slot{"proposes": "espresso martini,moscow mule,dirty martini,vesper,sea breeze,screwdriver,kamikaze,harvey wallbanger,french martini,long island iced tea,bloody mary,russian spring punch"}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - choice_form
    - form{"name": "choice_form"}
    - slot{"requested_slot": "cardinal"}
* form: cardinal{"cardinal": "3"}
    - slot{"cardinal": "3"}
    - choice_form
    - slot{"cardinal": 2}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "dirty martini"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_ask_something_else
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## fail search
* search_provider{"category": "cocktail", "ingredient": "juice"}
    - slot{"category": "cocktail"}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": []}
    - slot{"multiple_options": true}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": ""}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider{"ingredient": "grapefruit juice"}
    - form: search_form
    - slot{"ingredient": ["grapefruit juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "grapefruit juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider{"ingredient": "midori"}
    - form: search_form
    - slot{"ingredient": ["vodka"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "grapefruit juice,vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider{"ingredient": "dark rum"}
    - form: search_form
    - slot{"ingredient": ["dark rum"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "grapefruit juice,vodka,dark rum"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "grapefruit juice,vodka,dark rum"}
* affirm
    - action_search
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_ask_something_else
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## multiple explain in search
* search_provider
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider{"category": "cocktail", "ingredient": "vodka"}
    - slot{"category": "cocktail"}
    - form: search_form
    - slot{"ingredient": ["gin", "vodka"]}
    - slot{"category": "cocktail"}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin,vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* explain{"cocktail": "negroni"}
    - slot{"cocktail": "negroni"}
    - action_explain
    - slot{"cocktail": "negroni"}
    - utter_ask_continue
* affirm
    - search_form
    - slot{"requested_slot": "ingredient"}
* explain{"cocktail": "vesper"}
    - slot{"cocktail": "nvesper"}
    - action_explain
    - slot{"cocktail": "vesper"}
    - utter_ask_continue
* affirm
    - search_form
    - slot{"requested_slot": "ingredient"}
* explain{"cocktail": "spritz"}
    - slot{"cocktail": "spritz"}
    - action_explain
    - slot{"cocktail": "spritz"}
    - utter_ask_continue
* affirm
    - search_form
    - slot{"requested_slot": "ingredient"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "gin,vodka"}
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "gin,vodka"}
    - slot{"proposes": "vesper,long island iced tea"}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - choice_form
    - form{"name": "choice_form"}
    - slot{"requested_slot": "cardinal"}
* form: cardinal{"cardinal": "2"}
    - slot{"cardinal": "2"}
    - choice_form
    - slot{"cardinal": 1}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "long island iced tea"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation
* affirm
    - action_explain
    - slot{"cocktail": "long island iced tea"}
* thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_you_are_welcome_ask_something_else
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## multiple explain in choice 2 options
* search_provider{"category": "cocktail", "ingredient": "vodka"}
    - slot{"category": "cocktail"}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["gin", "vodka"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin,vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "gin,vodka"}
* affirm
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "gin,vodka"}
    - slot{"proposes": "vesper,long island iced tea"}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - choice_form
    - form{"name": "choice_form"}
    - slot{"requested_slot": "cardinal"}
* explain{"cocktail": "vesper"}
    - slot{"cocktail": "vesper"}
    - action_explain
    - slot{"cocktail": "vesper"}
    - action_continue
* explain{"cocktail": "negroni"}
    - slot{"cocktail": "negroni"}
    - action_explain
    - slot{"cocktail": "negroni"}
    - action_continue
* explain{"cocktail": "long island iced tea"}
    - slot{"cocktail": "long island iced tea"}
    - action_explain
    - slot{"cocktail": "long island iced tea"}
    - action_continue
    - action_listen
* form: cardinal{"cardinal": "1"}
    - slot{"cardinal": "1"}
    - choice_form
    - slot{"cardinal": 0}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "vesper"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_ask_something_else
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## just explain
* greet
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_how_can_i_help
* explain{"cocktail": "margarita"}
    - slot{"cocktail": "margarita"}
    - action_explain
    - slot{"cocktail": "margarita"}
* thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_you_are_welcome_ask_something_else
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye

## just preparation
* greet
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_how_can_i_help
* ask_preparation{"cocktail": "moscow mule"}
    - slot{"cocktail": "moscow mule"}
    - action_preparation
    - slot{"cocktail": "moscow mule"}
* thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_you_are_welcome_ask_something_else
* goodbye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - reset_slots
    - utter_goodbye
