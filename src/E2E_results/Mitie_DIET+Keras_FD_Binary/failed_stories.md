## Story 8 (tests/conversation_tests.md)
* search_provider: i have [vodka](ingredient)
    - search_form
    - form{"name": "search_form"}
    - slot{"ingredient": ["vodka"]}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "category"}
* form: search_provider: a [cocktail](category)
    - form: search_form
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "vodka"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka"}
    - slot{"proposes": "kamikaze,espresso martini,screwdriver"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka"}
    - slot{"proposes": "kamikaze,espresso martini,screwdriver,moscow mule,russian spring punch,vesper"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* deny: no
    - choice_form
    - form{"name": "choice_form"}
    - action_listen
    - slot{"requested_slot": "cardinal"}
* form: cardinal: the [4](cardinal)   <!-- predicted: explain: the [4](cocktail) -->
    - slot{"cocktail": "4"}
    - slot{"cardinal": "4"}
    - choice_form
    - slot{"cardinal": 3}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "moscow mule"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation   <!-- predicted: action_listen -->
* affirm: yes please
    - action_explain
    - slot{"cocktail": "moscow mule"}
* ask_preparation: prepare it
    - action_preparation
    - slot{"cocktail": "moscow mule"}


## Story 9 (tests/conversation_tests.md)
* ask_preparation: prepare [mojito](cocktail)
    - slot{"cocktail": "mojito"}
    - slot{"cocktail": "mojito"}
    - action_preparation
    - slot{"cocktail": "mojito"}
* ask_repeat: repeat
    - action_repeat
* search_provider: i want a [cocktail](category) with [juice](ingredient)
    - search_form
    - form{"name": "search_form"}
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
* form: search_provider: [Tomato juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["tomato juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "tomato juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "tomato juice"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "tomato juice"}
    - slot{"proposes": "vampiro,bloody mary"}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - choice_form
    - form{"name": "choice_form"}
    - action_listen
    - slot{"requested_slot": "cardinal"}
* form: cardinal: the [2](cardinal) one   <!-- predicted: cardinal: the [2](cocktail) one -->
    - slot{"cocktail": "2"}
    - slot{"cardinal": "2"}
    - choice_form
    - slot{"cardinal": 1}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "bloody mary"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation
* affirm: yes
    - action_explain
    - slot{"cocktail": "bloody mary"}
* ask_preparation: prepare it
    - action_preparation
    - slot{"cocktail": "bloody mary"}


## Story 10 (tests/conversation_tests.md)
* search_provider: i want a [cocktial](category)   <!-- predicted: search_provider: i want a [cocktial](cocktail) -->
    - slot{"cocktail": "cocktial"}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": null}
    - slot{"requested_slot": "category"}
* form: search_provider: [shot](category)
    - form: search_form
    - slot{"category": "shot"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [juice](ingredient)
    - form: search_form
    - slot{"ingredient": []}
    - slot{"multiple_options": true}
    - slot{"category": "shot"}
    - slot{"ingredient": null}
    - slot{"ingr_list": ""}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "shot"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [grapefruit juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["grapefruit juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "shot"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "grapefruit juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "shot"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "grapefruit juice"}
* affirm: yes
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
    - utter_ask_something_else
* deny: no thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 11 (tests/conversation_tests.md)
* search_provider: show [some](cocktail) info [about[bloody mary](cocktail) bloody mary   <!-- predicted: search_provider: show some info about[[bloody mary](cocktail) [bloody mary](cocktail) -->
    - slot{"cocktail": "bloody mary"}
    - slot{"cocktail": "bloody mary"}
    - search_form   <!-- predicted: action_explain -->
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: deny: no one
    - form: action_deactivate_form   <!-- predicted: search_form -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm   <!-- predicted: action_listen -->
    - slot{"ingr_list": ""}
* search_provider: tell me something [about](cocktail) [bloody mary](cocktail)   <!-- predicted: search_provider: tell me something about [bloody mary](cocktail) -->
    - slot{"cocktail": "bloody mary"}
    - slot{"cocktail": "bloody mary"}
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: explain: [bloody mary](cocktail)   <!-- predicted: ask_preparation: [bloody mary](cocktail) -->
    - slot{"cocktail": "bloody mary"}
    - slot{"cocktail": "bloody mary"}
    - form: action_explain   <!-- predicted: search_form -->
    - slot{"cocktail": "bloody mary"}
    - form: action_listen   <!-- predicted: search_form -->
* form: thanks: thank you
    - form: action_deactivate_form   <!-- predicted: search_form -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots   <!-- predicted: action_listen -->
    - utter_you_are_welcome_ask_something_else   <!-- predicted: search_form -->
* affirm: yes
    - action_search   <!-- predicted: action_deactivate_form -->
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"proposes": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots   <!-- predicted: action_ask_confirm -->
    - utter_goodbye   <!-- predicted: action_search -->


## Story 12 (tests/conversation_tests.md)
* ask_preparation: prepare me something
    - action_preparation
    - slot{"cocktail": null}
* ask_preparation: prepare me [long island iced tea](cocktail)
    - slot{"cocktail": "long island iced tea"}
    - slot{"cocktail": "long island iced tea"}
    - action_preparation
    - slot{"cocktail": "long island iced tea"}
* search_provider: i have [milk](ingredient) and [ginger](ingredient)
    - search_form
    - form{"name": "search_form"}
    - slot{"ingredient": ["milk"]}
    - slot{"multiple_options": true}
    - slot{"requested_slot": "category"}
* form: search_provider: [ginger ale](ingredient)   <!-- predicted: search_provider: [ginger](ingredient) [ale](ingredient) -->
    - form: search_form
    - slot{"ingredient": ["ginger ale"]}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "category"}
* form: search_provider: [cocktail](category)
    - form: search_form
    - slot{"category": "cocktail"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "ginger ale"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "ginger ale"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "ginger ale"}
    - slot{"proposes": "moscow mule,horse's neck"}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - choice_form   <!-- predicted: action_listen -->
    - form{"name": "choice_form"}
    - action_listen
    - slot{"requested_slot": "cardinal"}
* form: cardinal: the [2](cardinal)   <!-- predicted: explain: the [2](cocktail) -->
    - slot{"cocktail": "2"}
    - slot{"cardinal": "2"}
    - choice_form
    - slot{"cardinal": 1}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "horse's neck"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation   <!-- predicted: action_listen -->
* deny: no
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_ask_something_else
* explain: explain [horse's neck](cocktail)
    - slot{"cocktail": "horse's neck"}
    - slot{"cocktail": "horse's neck"}
    - action_explain
    - slot{"cocktail": "horse's neck"}
* ask_preparation: prepare it
    - action_preparation
    - slot{"cocktail": "horse's neck"}
* thanks: thank you
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* deny: no
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 13 (tests/conversation_tests.md)
* search_provider: i a want a [coffee](ingredient) [cocktail](category)   <!-- predicted: search_provider: i a want a [coffee](cocktail) [cocktail](category) -->
    - slot{"cocktail": "coffee"}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["coffee"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "coffee"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [milk](ingredient)
    - form: search_form
    - slot{"ingredient": ["milk"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "coffee,milk"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "coffee,milk"}
* affirm: yes
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
    - utter_ask_something_else
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 14 (tests/conversation_tests.md)
* ask_functions: what can you do
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_explain_functions
* search_provider: [vodka](ingredient) and [gin](ingredient) [cocktail](category)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["vodka", "gin"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka,gin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* explain: explain [tequila sunrise](cocktail)
    - slot{"cocktail": "tequila sunrise"}
    - slot{"cocktail": "tequila sunrise"}
    - action_explain
    - slot{"cocktail": "tequila sunrise"}
    - action_listen   <!-- predicted: utter_ask_continue -->
    - action_listen
* form: search_provider: add [orange juice](ingredient)
    - search_form
    - slot{"ingredient": ["orange juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka,gin,orange juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_explain -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "vodka,gin,orange juice"}
* affirm: yes
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
    - utter_ask_something_else
* goodbye: bye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 15 (tests/conversation_tests.md)
* ask_preparation: prepare a [cocktail](category)
    - action_preparation   <!-- predicted: search_form -->
    - slot{"cocktail": null}
* ask_preparation: prepare [mojito](cocktail)
    - slot{"cocktail": "mojito"}
    - slot{"cocktail": "mojito"}
    - action_preparation
    - slot{"cocktail": "mojito"}
* explain: explain it
    - action_explain
    - slot{"cocktail": "mojito"}
* search_provider: [shot](category) drink   <!-- predicted: search_provider: [shot drink](category) -->
    - search_form
    - form{"name": "search_form"}
    - slot{"category": null}
    - slot{"requested_slot": "category"}
* form: search_provider: [shot](category)
    - form: search_form
    - slot{"category": "shot"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [khlua](ingredient)
    - form: search_form
    - slot{"ingredient": null}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [kalhua](ingredient)   <!-- predicted: search_provider: kalhua -->
    - form: search_form
    - slot{"ingredient": null}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "ingredient"}
* affirm: [bayleis](cocktail)   <!-- predicted: explain: bayleis -->
    - slot{"cocktail": "bayleis"}
    - action_explain
    - slot{"cocktail": null}
    - utter_ask_continue
* deny: no
    - action_deactivate_form   <!-- predicted: search_form -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots   <!-- predicted: action_ask_confirm -->
    - utter_ask_something_else   <!-- predicted: action_listen -->
* goodbye: bye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye   <!-- predicted: utter_ask_something_else -->


## Story 16 (tests/conversation_tests.md)
* search_provider: [cocktail](category) with [min](ingr[rum](ingredient)ent) and rum   <!-- predicted: search_provider: [cocktail](category) with [minent](ingredient)) and [rum](ingredient) -->
    - search_form
    - form{"name": "search_form"}
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
* form: search_provider: [light rum](ingredient) and [mint](ingredient)
    - form: search_form
    - slot{"ingredient": ["light rum", "mint"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "light rum,mint"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [ice](ingredient) and [tonic](ingredient)   <!-- predicted: search_provider: [ice](cocktail) and tonic -->
    - slot{"cocktail": "ice"}
    - form: search_form
    - slot{"ingredient": ["ice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "light rum,mint,ice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: ask_ingredients: list ingredients
    - form: action_list_ingredients   <!-- predicted: search_form -->
    - slot{"ingr_list": "light rum,mint,ice"}
    - form: utter_ask_continue   <!-- predicted: search_form -->
    - form: action_listen   <!-- predicted: search_form -->
* form: affirm: yes
    - form: search_form
    - slot{"requested_slot": "ingredient"}
* deny: stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "light rum,mint,ice"}
* affirm: yes
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
    - utter_ask_something_else
* explain: explain [mojito](cocktail)
    - slot{"cocktail": "mojito"}
    - slot{"cocktail": "mojito"}
    - action_explain
    - slot{"cocktail": "mojito"}
* goodbye: thank you bye
    - action_deactivate_form   <!-- predicted: action_preparation -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 18 (tests/conversation_tests.md)
* greet: hi bot
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_how_can_i_help
* search_provider: i want a [cocktail](category) with [dry vermouth](ingredient)   <!-- predicted: search_provider: i want a [cocktail](category) with [dry vermouth](cocktail) -->
    - slot{"cocktail": "dry vermouth"}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["dry vermouth"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "dry vermouth"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [lime juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["lime juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "dry vermouth,lime juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [lemon peel](ingredient)
    - form: search_form
    - slot{"ingredient": ["lemon peel"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "dry vermouth,lime juice,lemon peel"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "dry vermouth,lime juice,lemon peel"}
* affirm: yes
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
    - utter_ask_something_else
* explain: explain [meingway special](cocktail)
    - slot{"cocktail": "meingway special"}
    - slot{"cocktail": "meingway special"}
    - action_explain
    - slot{"cocktail": null}
* explain: explain [hemingway special](cocktail)
    - slot{"cocktail": "hemingway special"}
    - slot{"cocktail": "hemingway special"}
    - action_explain   <!-- predicted: action_preparation -->
    - slot{"cocktail": "hemingway special"}
* goodbye: thank you bye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 19 (tests/conversation_tests.md)
* ask_functions: what can you do
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_explain_functions
* search_provider: i want  a [punch](category)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "punch"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [olive](ingredient)
    - form: search_form
    - slot{"ingredient": []}
    - slot{"multiple_options": true}
    - slot{"category": "punch"}
    - slot{"ingredient": null}
    - slot{"ingr_list": ""}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "punch"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [olive](ingredient)
    - form: search_form
    - slot{"ingredient": ["olive"]}
    - slot{"multiple_options": false}
    - slot{"category": "punch"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "olive"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "punch"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [brandy](ingredient)
    - form: search_form
    - slot{"ingredient": []}
    - slot{"multiple_options": true}
    - slot{"category": "punch"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "olive"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "punch"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [brandy](ingredient)
    - form: search_form
    - slot{"ingredient": ["brandy"]}
    - slot{"multiple_options": false}
    - slot{"category": "punch"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "olive,brandy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "punch"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [sugar syrum](ingredient) and [campari](ingredient)
    - form: search_form
    - slot{"ingredient": ["campari"]}
    - slot{"multiple_options": false}
    - slot{"category": "punch"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "olive,brandy,campari"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "punch"}
    - slot{"requested_slot": "ingredient"}
* ask_ingredients: what ingredients did i choose
    - action_list_ingredients
    - slot{"ingr_list": "olive,brandy,campari"}
    - utter_ask_continue
* affirm: yes
    - search_form
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "olive,brandy,campari"}
* affirm: yes please
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
    - utter_ask_something_else
* explain: explain [yolk](cocktail)   <!-- predicted: explain: explain [yolk](ingredient) -->
    - slot{"cocktail": "yolk"}
    - action_explain
    - slot{"cocktail": null}
* explain: explan [derby](cocktail)
    - slot{"cocktail": "derby"}
    - slot{"cocktail": "derby"}
    - action_explain   <!-- predicted: action_preparation -->
    - slot{"cocktail": "derby"}


## Story 20 (tests/conversation_tests.md)
* greet: good evening
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_how_can_i_help
* search_provider: i want a [cocktail](category)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [orang bitter](ingredient)   <!-- predicted: search_provider: [orang](ingredient) [bitter](cocktail) -->
    - slot{"cocktail": "bitter"}
    - form: search_form
    - slot{"ingredient": null}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [orange bitter](ingredient)   <!-- predicted: search_provider: [orange](ingredient) [bitter](cocktail) -->
    - slot{"cocktail": "bitter"}
    - form: search_form
    - slot{"ingredient": ["orange bitter"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "orange bitter"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [lime juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["lime juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "orange bitter,lime juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: ask_ingredients: show me ingredients i take
    - form: action_list_ingredients   <!-- predicted: search_form -->
    - slot{"ingr_list": "orange bitter,lime juice"}
    - form: utter_ask_continue   <!-- predicted: action_listen -->
* form: affirm: yes
    - form: search_form
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [gin](ingredient)
    - form: search_form
    - slot{"ingredient": ["gin"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "orange bitter,lime juice,gin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: ask_ingredients: show ingredients
    - form: action_list_ingredients   <!-- predicted: search_form -->
    - slot{"ingr_list": "orange bitter,lime juice,gin"}
    - form: utter_ask_continue   <!-- predicted: action_listen -->
* form: affirm: yes
    - form: search_form
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "orange bitter,lime juice,gin"}
* affirm: yes
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
    - utter_ask_something_else
* search_provider: [cocktail](category) with [ginger ale](ingredient)   <!-- predicted: search_provider: [cocktail](category) with [ginger](ingredient) [ale](ingredient) -->
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["ginger ale"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "ginger ale"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "ginger ale"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "ginger ale"}
    - slot{"proposes": "horse's neck,moscow mule"}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - choice_form   <!-- predicted: action_listen -->
    - form{"name": "choice_form"}
    - action_listen
    - slot{"requested_slot": "cardinal"}
* form: cardinal: the [firs](cardinal)   <!-- predicted: cardinal: the [firs](ingredient) -->
    - slot{"cardinal": "firs"}
    - choice_form
* form: explain: [1](cocktail)   <!-- predicted: thanks: [1](cocktail) -->
    - slot{"cocktail": "1"}
    - slot{"cocktail": "1"}
    - form: action_explain   <!-- predicted: choice_form -->
    - slot{"cocktail": null}
    - form: choice_form   <!-- predicted: action_listen -->
* form: goodbye: bye
    - form: action_deactivate_form   <!-- predicted: choice_form -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots   <!-- predicted: choice_form -->
    - utter_goodbye   <!-- predicted: choice_form -->


## Story 21 (tests/conversation_tests.md)
* search_provider: [cocktail](category) with [orange peel](ingr[lemon juice](ingredient) lemon juice   <!-- predicted: search_provider: [cocktail](category) with [orange peel](ingredient) [lemon juice](ingredient) -->
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["orange peel", "lemon juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "orange peel,lemon juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: nothing
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "orange peel,lemon juice"}
* affirm: yes
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
    - utter_ask_something_else
* ask_preparation: preapre [tuxedo cocktail](cocktail)
    - slot{"cocktail": "tuxedo cocktail"}
    - slot{"cocktail": "tuxedo cocktail"}
    - action_preparation
    - slot{"cocktail": "tuxedo cocktail"}
* goodbye: bye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 22 (tests/conversation_tests.md)
* search_provider: [drink](category)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": null}
    - slot{"requested_slot": "category"}
* form: search_provider: [cocktail](category) with [gin](ingredient)
    - form: search_form
    - slot{"ingredient": ["gin"]}
    - slot{"category": "cocktail"}
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
* form: search_provider: [sugar](ingredient)
    - form: search_form
    - slot{"ingredient": []}
    - slot{"multiple_options": true}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [sugar](ingredient)
    - form: search_form
    - slot{"ingredient": ["sugar"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin,sugar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [cointreau](ingredient)
    - form: search_form
    - slot{"ingredient": ["cointreau"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "gin,sugar,cointreau"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "gin,sugar,cointreau"}
* affirm: yes
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
    - utter_ask_something_else
* goodbye: bye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 23 (tests/conversation_tests.md)
* ask_functions: funtionalities
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_explain_functions
* search_provider: i want a dirnk
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider: [cocktail](category)
    - form: search_form
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [brandy](ingredient) and [bourbon](ingredient)
    - form: search_form
    - slot{"ingredient": ["bourbon"]}
    - slot{"multiple_options": true}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "bourbon"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [brandy](ingredient)
    - form: search_form
    - slot{"ingredient": ["brandy"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "bourbon,brandy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [vodka](ingredient)
    - form: search_form
    - slot{"ingredient": ["vodka"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "bourbon,brandy,vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "bourbon,brandy,vodka"}
* affirm: yes
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
    - utter_ask_something_else
* search_provider: [cocktail](category) with [timato juice](ingredient)
    - search_form
    - form{"name": "search_form"}
    - action_listen
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [tomato juice](ingredient)
    - search_form
    - slot{"ingredient": ["tomato juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "tomato juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "tomato juice"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "tomato juice"}
    - slot{"proposes": "bloody mary,vampiro"}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - choice_form   <!-- predicted: action_listen -->
    - form{"name": "choice_form"}
    - slot{"requested_slot": "cardinal"}
* explain: [vampiro](cocktail)   <!-- predicted: search_provider: [vampiro](cocktail) -->
    - slot{"cocktail": "vampiro"}
    - slot{"cocktail": "vampiro"}
    - action_explain   <!-- predicted: choice_form -->
    - slot{"cocktail": "vampiro"}
    - action_continue   <!-- predicted: action_listen -->
    - action_listen
* form: cardinal: the [2](cardinal) one   <!-- predicted: cardinal: the [2](cocktail) one -->
    - slot{"cocktail": "2"}
    - slot{"cardinal": "2"}
    - choice_form
    - slot{"cardinal": 1}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "vampiro"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation   <!-- predicted: action_listen -->
* affirm: yes
    - action_explain
    - slot{"cocktail": "vampiro"}
* ask_preparation: prepare it
    - action_preparation
    - slot{"cocktail": "vampiro"}


## Story 24 (tests/conversation_tests.md)
* ask_preparation: preapre [grasshopper](cocktail)
    - slot{"cocktail": "grasshopper"}
    - slot{"cocktail": "grasshopper"}
    - action_preparation
    - slot{"cocktail": "grasshopper"}
* search_provider: [cocktail](category) with [egg white](ingredient)   <!-- predicted: search_provider: [cocktail](category) with [egg](ingredient) [white](ingredient) -->
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["egg white"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "egg white"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "egg white"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "egg white"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "clover club"}
    - utter_ask_explanation
* ask_preparation: prepare it
    - action_preparation   <!-- predicted: action_explain -->
    - slot{"cocktail": "clover club"}
* goodbye: thank you bye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 25 (tests/conversation_tests.md)
* search_provider: i want a [cocktail](category)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [cranberry juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["cranberry juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "cranberry juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [cranberry juice](ingredient)
    - form: search_form
    - slot{"ingredient": []}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "cranberry juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [amaretto](ingredient)
    - form: search_form
    - slot{"ingredient": ["amaretto"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "cranberry juice,amaretto"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* affirm: i'm ok   <!-- predicted: deny: i'm ok -->
    - action_search   <!-- predicted: action_deactivate_form -->
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - action_listen   <!-- predicted: action_ask_confirm -->
    - action_listen
* form: search_provider: [cocktail](category) with [tequila](ingr[lime](ingredient)nt) and lime   <!-- predicted: search_provider: [cocktail](category) with [tequilant](ingredient)) and [lime](ingredient) -->
    - search_form
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["tequila"]}
    - slot{"multiple_options": true}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "tequila"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [lime](ingredient)
    - form: search_form
    - slot{"ingredient": ["lime"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "tequila,lime"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: thanks: that's all   <!-- predicted: affirm: that['s](cocktail) all -->
    - slot{"cocktail": "'s"}
    - form: action_default_fallback   <!-- predicted: search_form -->
* form: ask_ingredients: no more ingredients
    - form: action_list_ingredients   <!-- predicted: search_form -->
    - slot{"ingr_list": "tequila,lime"}
    - form: utter_ask_continue   <!-- predicted: action_listen -->
* form: affirm: yes
    - form: search_form
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm   <!-- predicted: action_reset_all_slots -->
    - slot{"ingr_list": "tequila,lime"}
* affirm: yes
    - action_search   <!-- predicted: action_explain -->
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - action_deactivate_form   <!-- predicted: action_listen -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_ask_something_else
* goodbye: no more bye   <!-- predicted: affirm: no more bye -->
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 27 (tests/conversation_tests.md)
* ask_functions: what can you do
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_explain_functions
* search_provider: i want a [cocktail](category)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [pineapple huice](ingredient)
    - form: search_form
    - slot{"ingredient": null}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [pineapple juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["pineapple juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "pineapple juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [granadine](ingredient)
    - form: search_form
    - slot{"ingredient": null}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "ingredient"}
* ask_ingredients: which ingredients do i choose
    - action_list_ingredients
    - slot{"ingr_list": "pineapple juice"}
    - utter_ask_continue
* affirm: yes
    - search_form
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [grenadine](ingredient)
    - form: search_form
    - slot{"ingredient": ["grenadine"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "pineapple juice,grenadine"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [maraschino liqueur](ingredient)   <!-- predicted: search_provider: [maraschino liqueur](cocktail) -->
    - slot{"cocktail": "maraschino liqueur"}
    - form: search_form
    - slot{"ingredient": ["maraschino liqueur"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "pineapple juice,grenadine,maraschino liqueur"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "pineapple juice,grenadine,maraschino liqueur"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "pineapple juice,grenadine,maraschino liqueur"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "mary pickford"}
    - utter_ask_explanation
* affirm: yes please
    - action_explain
    - slot{"cocktail": "mary pickford"}
* explain: could you explain [horse's neck](cocktail)
    - slot{"cocktail": "horse's neck"}
    - slot{"cocktail": "horse's neck"}
    - action_explain
    - slot{"cocktail": "horse's neck"}
* ask_preparation: prepare [dirty martini](cocktail) please
    - slot{"cocktail": "dirty martini"}
    - slot{"cocktail": "dirty martini"}
    - action_preparation
    - slot{"cocktail": "dirty martini"}
* thanks: by thank you
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* goodbye: bye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 28 (tests/conversation_tests.md)
* greet: hi bot
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_how_can_i_help
* ask_functions: how can you help me
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_explain_functions
* ask_preparation: prepare [long island iced tea](cocktail) please
    - slot{"cocktail": "long island iced tea"}
    - slot{"cocktail": "long island iced tea"}
    - action_preparation
    - slot{"cocktail": "long island iced tea"}
* thanks: thank you
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* goodbye: no more bye   <!-- predicted: affirm: no more bye -->
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye   <!-- predicted: utter_explain_functions -->


## Story 29 (tests/conversation_tests.md)
* greet: hey bot
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_how_can_i_help
* ask_functions: show ducntionalities
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_explain_functions
* explain: what is [golden dream](cocktail)
    - slot{"cocktail": "golden dream"}
    - slot{"cocktail": "golden dream"}
    - action_explain
    - slot{"cocktail": "golden dream"}
* ask_preparation: thank you, prepare [horse's neck](cocktail)   <!-- predicted: ask_preparation: thank you[,](cocktail) prepare [horse's neck](cocktail) -->
    - slot{"cocktail": "horse's neck"}
    - slot{"cocktail": "horse's neck"}
    - action_preparation
    - slot{"cocktail": "horse's neck"}
* thanks: thank you
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* goodbye: no bye   <!-- predicted: affirm: no bye -->
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye   <!-- predicted: utter_explain_functions -->


## Story 30 (tests/conversation_tests.md)
* greet: hello
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_how_can_i_help
* search_provider: i want to drink now
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider: a [cocktail](category) with [lime juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["lime juice"]}
    - slot{"category": "cocktail"}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lime juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [grapefruit juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["grapefruit juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lime juice,grapefruit juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* ask_ingredients: list ingredients
    - action_list_ingredients
    - slot{"ingr_list": "lime juice,grapefruit juice"}
    - utter_ask_continue
* affirm: yes
    - search_form
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "lime juice,grapefruit juice"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "lime juice,grapefruit juice"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "hemingway special"}
    - utter_ask_explanation
* affirm: yes please
    - action_explain
    - slot{"cocktail": "hemingway special"}
* ask_preparation: how can i prepare it
    - action_preparation
    - slot{"cocktail": "hemingway special"}
* goodbye: bye
    - action_deactivate_form   <!-- predicted: action_repeat -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 31 (tests/conversation_tests.md)
* greet: hello man   <!-- predicted: greet: hello [man](cocktail) -->
    - slot{"cocktail": "man"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_how_can_i_help
* explain: explain [spritz](cocktail)
    - slot{"cocktail": "spritz"}
    - slot{"cocktail": "spritz"}
    - action_explain
    - slot{"cocktail": "spritz"}
* thanks: thank you man   <!-- predicted: thanks: thank you [man](cocktail) -->
    - slot{"cocktail": "man"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* goodbye: bye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 31 (tests/conversation_tests.md)
* search_provider: i want a [cocktail](category)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [coffee](ingredient) and [irish whiskey](ingredient)   <!-- predicted: explain: [coffee](ingredient) and [irish whiskey](ingredient) -->
    - form: search_form
    - slot{"ingredient": ["coffee", "irish whiskey"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "coffee,irish whiskey"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "coffee,irish whiskey"}
* affirm: yes please
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "coffee,irish whiskey"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "irish coffee"}
    - utter_ask_explanation
* ask_preparation: prepare it
    - action_preparation   <!-- predicted: action_explain -->
    - slot{"cocktail": "irish coffee"}
* goodbye: bye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 32 (tests/conversation_tests.md)
* ask_functions: hey bot what can you do
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_explain_functions
* explain: what is [cosmopolitan](cocktail)
    - slot{"cocktail": "cosmopolitan"}
    - slot{"cocktail": "cosmopolitan"}
    - action_explain
    - slot{"cocktail": "cosmopolitan"}
* ask_preparation: can you prepare [french martini](cocktail)
    - slot{"cocktail": "french martini"}
    - slot{"cocktail": "french martini"}
    - action_preparation
    - slot{"cocktail": "french martini"}
* thanks: thank you bot
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* goodbye: no more, bye   <!-- predicted: goodbye: no more[,](cocktail) bye -->
    - slot{"cocktail": ","}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 34 (tests/conversation_tests.md)
* ask_functions: how can you help
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_explain_functions
* search_provider: i want a [cocktail](category)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [vermouth](ingredient) and [olive](ingredient)
    - form: search_form
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
* form: search_provider: [dry vermouth](ingredient) and [olive](ingredient)   <!-- predicted: search_provider: [dry vermouth](cocktail) and [olive](ingredient) -->
    - slot{"cocktail": "dry vermouth"}
    - form: search_form
    - slot{"ingredient": ["dry vermouth", "olive"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "dry vermouth,olive"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [gin](ingredient)
    - form: search_form
    - slot{"ingredient": ["gin"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "dry vermouth,olive,gin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "dry vermouth,olive,gin"}
* affirm: yes please
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "dry vermouth,olive,gin"}
    - slot{"proposes": "martini,dry martini"}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - choice_form
    - form{"name": "choice_form"}
    - action_listen
    - slot{"requested_slot": "cardinal"}
* form: cardinal: the [2](cardinal) one   <!-- predicted: cardinal: the [2](cocktail) one -->
    - slot{"cocktail": "2"}
    - slot{"cardinal": "2"}
    - choice_form
    - slot{"cardinal": 1}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "dry martini"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation
* affirm: yes please
    - action_explain
    - slot{"cocktail": "dry martini"}
* ask_preparation: can you prepare it
    - action_preparation
    - slot{"cocktail": "dry martini"}
* ask_preparation: how can i prepare [long island iced tea](cocktail)
    - slot{"cocktail": "long island iced tea"}
    - slot{"cocktail": "long island iced tea"}
    - action_preparation
    - slot{"cocktail": "long island iced tea"}
* thanks: thank you bot very helpful
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* deny: no more thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 35 (tests/conversation_tests.md)
* search_provider: i want to drink something
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider: a [cocktail](category)
    - form: search_form
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [creme de cassis](ingredient) and [vodka](ingredient)
    - form: search_form
    - slot{"ingredient": ["creme de cassis", "vodka"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "creme de cassis,vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [syrup](ingredient)
    - form: search_form
    - slot{"ingredient": []}
    - slot{"multiple_options": true}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "creme de cassis,vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [sugar syrup](ingredient)
    - form: search_form
    - slot{"ingredient": ["sugar syrup"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "creme de cassis,vodka,sugar syrup"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: deny: nothing more thank you   <!-- predicted: thanks: nothing more thank you -->
    - form: action_deactivate_form   <!-- predicted: search_form -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm   <!-- predicted: action_listen -->
    - slot{"ingr_list": "creme de cassis,vodka,sugar syrup"}
* affirm: yes please
    - action_search   <!-- predicted: action_deactivate_form -->
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "creme de cassis,vodka,sugar syrup"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "russian spring punch"}
    - utter_ask_explanation   <!-- predicted: action_ask_confirm -->
* affirm: oh yes   <!-- predicted: greet: oh yes -->
    - action_explain   <!-- predicted: action_deactivate_form -->
    - slot{"cocktail": "russian spring punch"}
    - action_listen   <!-- predicted: action_reset_all_slots -->
* goodbye: thank you bye
    - action_deactivate_form   <!-- predicted: utter_ask_something_else -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye   <!-- predicted: utter_ask_something_else -->


## Story 36 (tests/conversation_tests.md)
* search_provider: i want a [cocktail](category) with [lemon juice](ingredient)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["lemon juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lemon juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [cognac](ingredient)
    - form: search_form
    - slot{"ingredient": ["cognac"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lemon juice,cognac"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [conitreau](ingredient)   <!-- predicted: search_provider: [conitreau](cocktail) -->
    - slot{"cocktail": "conitreau"}
    - form: search_form
    - slot{"ingredient": null}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [cointreau](ingredient)
    - form: search_form
    - slot{"ingredient": ["cointreau"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lemon juice,cognac,cointreau"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: nothing more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "lemon juice,cognac,cointreau"}
* affirm: yes please
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "lemon juice,cognac,cointreau"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "sidecar"}
    - utter_ask_explanation
* ask_preparation: prepare [harvey wallbanger](cocktail)
    - slot{"cocktail": "harvey wallbanger"}
    - slot{"cocktail": "harvey wallbanger"}
    - action_preparation   <!-- predicted: action_explain -->
    - slot{"cocktail": "harvey wallbanger"}
* goodbye: bye!   <!-- predicted: goodbye: bye[!](cocktail) -->
    - slot{"cocktail": "!"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 38 (tests/conversation_tests.md)
* search_provider: i want a [cocktail](category)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [lime juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["lime juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lime juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [rum](ingredient)
    - form: search_form
    - slot{"ingredient": []}
    - slot{"multiple_options": true}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lime juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [rum](ingredient)
    - form: search_form
    - slot{"ingredient": ["rum"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lime juice,rum"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [maraschino liqueur](ingredient)   <!-- predicted: search_provider: [maraschino liqueur](cocktail) -->
    - slot{"cocktail": "maraschino liqueur"}
    - form: search_form
    - slot{"ingredient": ["maraschino liqueur"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lime juice,rum,maraschino liqueur"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: ask_ingredients: list the ingredients
    - form: action_list_ingredients   <!-- predicted: search_form -->
    - slot{"ingr_list": "lime juice,rum,maraschino liqueur"}
    - form: utter_ask_continue   <!-- predicted: action_listen -->
* form: affirm: yes
    - form: search_form
    - slot{"requested_slot": "ingredient"}
* deny: no more thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "lime juice,rum,maraschino liqueur"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "lime juice,rum,maraschino liqueur"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "hemingway special"}
    - utter_ask_explanation
* affirm: yes please
    - action_explain
    - slot{"cocktail": "hemingway special"}
* goodbye: bye and thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 40 (tests/conversation_tests.md)
* search_provider: i want to drink
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider: a [cocktail](category) with [orange bitters](ingredient)
    - form: search_form
    - slot{"ingredient": ["orange bitters"]}
    - slot{"category": "cocktail"}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "orange bitters"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [cherry](ingredient) please   <!-- predicted: cardinal: [cherry](ingredient) please -->
    - form: search_form
    - slot{"ingredient": []}
    - slot{"multiple_options": true}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "orange bitters"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [cherry](ingredient)
    - form: search_form
    - slot{"ingredient": ["cherry"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "orange bitters,cherry"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: nothing else
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "orange bitters,cherry"}
* affirm: oh yeah   <!-- predicted: greet: oh yeah -->
    - action_search   <!-- predicted: action_deactivate_form -->
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "orange bitters,cherry"}
    - slot{"proposes": "casino,tuxedo cocktail"}
    - slot{"more_results": false}
    - slot{"cocktail": null}
    - choice_form
    - form{"name": "choice_form"}
    - slot{"requested_slot": "cardinal"}
* explain: explain [casino](cocktail)
    - slot{"cocktail": "casino"}
    - slot{"cocktail": "casino"}
    - action_explain
    - slot{"cocktail": "casino"}
    - action_continue
    - action_listen
* form: cardinal: the [2](cardinal) one   <!-- predicted: cardinal: the [2](cocktail) one -->
    - slot{"cocktail": "2"}
    - slot{"cardinal": "2"}
    - choice_form
    - slot{"cardinal": 1}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "tuxedo cocktail"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation
* affirm: yes please
    - action_explain   <!-- predicted: action_deactivate_form -->
    - slot{"cocktail": "tuxedo cocktail"}
* ask_preparation: prepare [cuba libre](cocktail) please
    - slot{"cocktail": "cuba libre"}
    - slot{"cocktail": "cuba libre"}
    - action_preparation
    - slot{"cocktail": "cuba libre"}
* goodbye: bye bot
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 41 (tests/conversation_tests.md)
* greet: good evening bot
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_how_can_i_help
* explain: how can i [make](cocktail) [golden dream](cocktail)   <!-- predicted: explain: how can i make [golden dream](cocktail) -->
    - slot{"cocktail": "golden dream"}
    - slot{"cocktail": "golden dream"}
    - action_explain
    - slot{"cocktail": "golden dream"}
* ask_preparation: prepare it please
    - action_preparation
    - slot{"cocktail": "golden dream"}
* thanks: thank you bot
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* deny: no i'm done
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 42 (tests/conversation_tests.md)
* search_provider: i want to drink
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider: a [cocktail](category) with [vodka](ingredient)
    - form: search_form
    - slot{"ingredient": ["vodka"]}
    - slot{"category": "cocktail"}
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
* form: search_provider: [galliano](ingredient) please
    - form: search_form
    - slot{"ingredient": ["galliano"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka,galliano"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* ask_ingredients: list ingredients
    - action_list_ingredients
    - slot{"ingr_list": "vodka,galliano"}
    - utter_ask_continue
* affirm: yes
    - search_form
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [orange juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["orange juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka,galliano,orange juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "vodka,galliano,orange juice"}
* affirm: yes please
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka,galliano,orange juice"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "harvey wallbanger"}
    - utter_ask_explanation
* affirm: ok
    - action_explain
    - slot{"cocktail": "harvey wallbanger"}
* ask_preparation: how can i prepare it
    - action_preparation
    - slot{"cocktail": "harvey wallbanger"}
* thanks: oh nice cardinal thank you   <!-- predicted: thanks: oh nice [cardinal](cocktail) thank you -->
    - slot{"cocktail": "cardinal"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* deny: no thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 44 (tests/conversation_tests.md)
* search_provider: i want a drink
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider: a [cocktail](category) with vo[vodka](ingr[gin](ingredient)ent)nd gin   <!-- predicted: search_provider: a [cocktail](category) with vovodkaent)[nd gin](ingredient) -->
    - form: search_form
    - slot{"ingredient": ["vodka", "gin"]}
    - slot{"category": "cocktail"}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka,gin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [lillet blanc](ingredient)
    - form: search_form
    - slot{"ingredient": ["lillet blanc"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "vodka,gin,lillet blanc"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: affirm: it's fine   <!-- predicted: affirm: it['s](cocktail) fine -->
    - slot{"cocktail": "'s"}
    - form: action_search   <!-- predicted: search_form -->
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka,gin,lillet blanc"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "vesper"}
    - form: utter_ask_continue   <!-- predicted: action_listen -->
* form: affirm: yes
    - form: search_form
    - slot{"requested_slot": "ingredient"}
* deny: no more thanks
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "vodka,gin,lillet blanc"}
* affirm: yes please
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "vodka,gin,lillet blanc"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "vesper"}
    - utter_ask_explanation
* explain: show me [some information](cocktail)   <!-- predicted: explain: show me some [information](cocktail) -->
    - slot{"cocktail": "information"}
    - slot{"cocktail": "some information"}
    - action_explain
    - slot{"cocktail": null}
    - action_listen   <!-- predicted: action_continue -->
* affirm: yes
    - action_explain   <!-- predicted: action_listen -->
    - slot{"cocktail": null}
* ask_preparation: prepare [negroni](cocktail)
    - slot{"cocktail": "negroni"}
    - slot{"cocktail": "negroni"}
    - action_preparation
    - slot{"cocktail": "negroni"}
* goodbye: bye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 45 (tests/conversation_tests.md)
* greet: good evening
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_how_can_i_help
* explain: what is [manhattan](cocktail)
    - slot{"cocktail": "manhattan"}
    - slot{"cocktail": "manhattan"}
    - action_explain
    - slot{"cocktail": "manhattan"}
* ask_preparation: can you prepare [stinger](cocktail)
    - slot{"cocktail": "stinger"}
    - slot{"cocktail": "stinger"}
    - action_preparation
    - slot{"cocktail": "stinger"}
* thanks: thank you sir
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* goodbye: no more, bye   <!-- predicted: goodbye: no more[,](cocktail) bye -->
    - slot{"cocktail": ","}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 46 (tests/conversation_tests.md)
* greet: hello
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_how_can_i_help
* search_provider: i want a [cocktail](category) with [sweet and sour](ingredient)   <!-- predicted: search_provider: i want a [cocktail](category) with [sweet](ingredient) and [sour](ingredient) -->
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["sweet and sour"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "sweet and sour"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [triple sec](ingredient) and [cherry](ingredient)
    - form: search_form
    - slot{"ingredient": ["triple sec"]}
    - slot{"multiple_options": true}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "sweet and sour,triple sec"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [cherry](ingredient)
    - form: search_form
    - slot{"ingredient": ["cherry"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "sweet and sour,triple sec,cherry"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: nothing more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "sweet and sour,triple sec,cherry"}
* affirm: yes please
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "sweet and sour,triple sec,cherry"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "mai tai"}
    - utter_ask_explanation
* ask_preparation: prepare it
    - action_preparation   <!-- predicted: action_explain -->
    - slot{"cocktail": "mai tai"}
* goodbye: thank you, bye   <!-- predicted: goodbye: thank you[,](cocktail) bye -->
    - slot{"cocktail": ","}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 47 (tests/conversation_tests.md)
* search_provider: [give](ingredient) me a [cocktail](category)   <!-- predicted: search_provider: give me a [cocktail](category) -->
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [pineapple juice](ingredient) and [maraschino cherry](ingredient)   <!-- predicted: search_provider: [pineapple juice and](ingredient) [maraschino](cocktail) [cherry](ingredient) -->
    - slot{"cocktail": "maraschino"}
    - form: search_form
    - slot{"ingredient": ["pineapple juice", "maraschino cherry"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "pineapple juice,maraschino cherry"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: nothing more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "pineapple juice,maraschino cherry"}
* affirm: ok
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "pineapple juice,maraschino cherry"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "mary pickford"}
    - utter_ask_explanation
* affirm: sure
    - action_search   <!-- predicted: action_explain -->
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "pineapple juice,maraschino cherry"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "mary pickford"}
    - utter_ask_explanation   <!-- predicted: action_listen -->
* affirm: yes
    - action_explain   <!-- predicted: action_listen -->
    - slot{"cocktail": "mary pickford"}
* goodbye: bye
    - action_deactivate_form   <!-- predicted: action_repeat -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 49 (tests/conversation_tests.md)
* search_provider: do you know [cocktail](category) with [lime juice](ingredient)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["lime juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lime juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [triple sec](ingredient) and [white rum](ingredient)
    - form: search_form
    - slot{"ingredient": ["triple sec", "white rum"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lime juice,triple sec,white rum"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* ask_ingredients: which ingredients did i choose
    - action_list_ingredients
    - slot{"ingr_list": "lime juice,triple sec,white rum"}
    - utter_ask_continue
* affirm: yes
    - search_form   <!-- predicted: action_deactivate_form -->
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [galliano](ingredient) please
    - form: search_form
    - slot{"ingredient": ["galliano"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lime juice,triple sec,white rum,galliano"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: i'm done
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "lime juice,triple sec,white rum,galliano"}
* affirm: sure
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "lime juice,triple sec,white rum,galliano"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "yellow bird"}
    - utter_ask_explanation
* explain: explain [cosmopolitan](cocktail)
    - slot{"cocktail": "cosmopolitan"}
    - slot{"cocktail": "cosmopolitan"}
    - action_explain
    - slot{"cocktail": "cosmopolitan"}
    - action_listen   <!-- predicted: action_continue -->
* goodbye: bye
    - action_deactivate_form   <!-- predicted: action_preparation -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 50 (tests/conversation_tests.md)
* search_provider: a [cocktail](category) with [cranberry juice](ingredient)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": ["cranberry juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "cranberry juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* explain: explain [russian spring punch](cocktail)
    - slot{"cocktail": "russian spring punch"}
    - slot{"cocktail": "russian spring punch"}
    - action_explain
    - slot{"cocktail": "russian spring punch"}
    - action_listen   <!-- predicted: utter_ask_continue -->
* ask_ingredients: list ingredients
    - action_list_ingredients   <!-- predicted: search_form -->
    - slot{"ingr_list": "cranberry juice"}
    - utter_ask_continue
    - action_listen
* form: affirm: yes
    - search_form
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [grapefruit juice](ingredient)
    - form: search_form
    - slot{"ingredient": ["grapefruit juice"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "cranberry juice,grapefruit juice"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: nothing more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "cranberry juice,grapefruit juice"}
* affirm: yes bot
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "cranberry juice,grapefruit juice"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "sea breeze"}
    - utter_ask_explanation
* affirm: yes please
    - action_explain
    - slot{"cocktail": "sea breeze"}
* goodbye: goodbye bot
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 3 (tests/conversation_tests.md)
* greet: hi
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_how_can_i_help
* ask_preparation: prepare [gin tonic](cocktail)   <!-- predicted: ask_preparation: prepare [gin](cocktail) tonic -->
    - slot{"cocktail": "gin"}
    - slot{"cocktail": "gin tonic"}
    - action_preparation
    - slot{"cocktail": null}
* search_provider: [cocktail](category) with [gin](ingredient)
    - search_form
    - form{"name": "search_form"}
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
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "gin"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "gin"}
    - slot{"proposes": "french 75,vesper,clover club"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "gin"}
    - slot{"proposes": "french 75,vesper,clover club,gin fizz,derby,tuxedo cocktail"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* ask_preparation: prepare [gin fizz](cocktail)
    - slot{"cocktail": "gin fizz"}
    - slot{"cocktail": "gin fizz"}
    - action_preparation   <!-- predicted: action_explain -->
    - slot{"cocktail": "gin fizz"}
* thanks: thank you
    - action_deactivate_form   <!-- predicted: choice_form -->
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots   <!-- predicted: choice_form -->
    - utter_you_are_welcome_ask_something_else
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye   <!-- predicted: action_listen -->


## Story 4 (tests/conversation_tests.md)
* explain: explain [vesper](cocktail)
    - slot{"cocktail": "vesper"}
    - slot{"cocktail": "vesper"}
    - action_explain
    - slot{"cocktail": "vesper"}
* ask_preparation: could you prepare a [cocktail](category)
    - action_preparation
    - slot{"cocktail": "vesper"}
* search_provider: show [cocktails](category) with [gin](ingredient)
    - search_form
    - form{"name": "search_form"}
    - slot{"category": null}
    - slot{"ingredient": ["gin"]}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "category"}
* form: search_provider: show [cocktail](category) with [gin](ingredient)
    - form: search_form
    - slot{"ingredient": ["gin"]}
    - slot{"category": "cocktail"}
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
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "gin"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "gin"}
    - slot{"proposes": "dry martini,rose,bramble"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* explain: no. explain [bramble](cocktail)   <!-- predicted: explain: no[.](cocktail) explain [bramble](cocktail) -->
    - slot{"cocktail": "bramble"}
    - slot{"cocktail": "bramble"}
    - action_explain
    - slot{"cocktail": "bramble"}
    - action_continue
* deny: no
    - choice_form   <!-- predicted: action_search -->
    - form{"name": "choice_form"}
    - action_listen
    - slot{"requested_slot": "cardinal"}
* form: cardinal: the [2](cardinal) one   <!-- predicted: cardinal: the [2](cocktail) one -->
    - slot{"cocktail": "2"}
    - slot{"cardinal": "2"}
    - choice_form
    - slot{"cardinal": 1}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "rose"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation
* affirm: yes
    - action_explain
    - slot{"cocktail": "rose"}
* thanks: thank you
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 5 (tests/conversation_tests.md)
* search_provider: hi i want to drink
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider: [shot](category)
    - form: search_form
    - slot{"category": "shot"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [lemon](ingredient)
    - form: search_form
    - slot{"ingredient": []}
    - slot{"multiple_options": true}
    - slot{"category": "shot"}
    - slot{"ingredient": null}
    - slot{"ingr_list": ""}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "shot"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [lemon peel](ingredient)
    - form: search_form
    - slot{"ingredient": ["lemon peel"]}
    - slot{"multiple_options": false}
    - slot{"category": "shot"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "lemon peel"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "shot"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "lemon peel"}
* affirm: yes
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
    - utter_ask_something_else
* search_provider: i want a [cocktail](category)
    - search_form
    - form{"name": "search_form"}
    - action_listen
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [orange](ingredient)
    - search_form
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
* form: search_provider: [orange bitters](ingredient)
    - form: search_form
    - slot{"ingredient": ["orange bitters"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "orange bitters"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [wiskey](ingredient)   <!-- predicted: search_provider: wiskey -->
    - form: search_form
    - slot{"ingredient": null}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "ingredient"}
* ask_ingredients: list ingredients
    - action_list_ingredients
    - slot{"ingr_list": "orange bitters"}
    - utter_ask_continue
* affirm: yes
    - search_form
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [vodka](ingredient)
    - form: search_form
    - slot{"ingredient": ["vodka"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "orange bitters,vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "orange bitters,vodka"}
* affirm: yes
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
    - utter_ask_something_else
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 6 (tests/conversation_tests.md)
* explain: i want a [mojito](cocktail)
    - slot{"cocktail": "mojito"}
    - slot{"cocktail": "mojito"}
    - action_explain
    - slot{"cocktail": "mojito"}
* ask_preparation: how can i prepare it
    - action_preparation
    - slot{"cocktail": "mojito"}
* thanks: thank you
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* ask_preparation: prepare [gin tonic](cocktail)   <!-- predicted: ask_preparation: prepare [gin](cocktail) tonic -->
    - slot{"cocktail": "gin"}
    - slot{"cocktail": "gin tonic"}
    - action_preparation
    - slot{"cocktail": null}
* search_provider: [cocktail](category) with [tonic](ingredient)   <!-- predicted: search_provider: [cocktail](category) with tonic -->
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"multiple_options": false}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [soda](ingredient)
    - form: search_form
    - slot{"ingredient": ["soda"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "soda"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [gin](ingredient)
    - form: search_form
    - slot{"ingredient": ["gin"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "soda,gin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "soda,gin"}
* affirm: yes
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
    - utter_ask_something_else
* search_provider: [cocktail](category) [gin](ingredient)
    - search_form
    - form{"name": "search_form"}
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
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "gin"}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "gin"}
    - slot{"proposes": "monkey gland,alexander,gin fizz"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* affirm: yes
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "gin"}
    - slot{"proposes": "monkey gland,alexander,gin fizz,white lady,martini,french 75"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* affirm: yes
    - action_search   <!-- predicted: action_explain -->
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "gin"}
    - slot{"proposes": "monkey gland,alexander,gin fizz,white lady,martini,french 75,tuxedo cocktail,negroni,casino"}
    - slot{"more_results": true}
    - slot{"cocktail": null}
* deny: no
    - choice_form
    - form{"name": "choice_form"}
    - action_listen
    - slot{"requested_slot": "cardinal"}
* form: cardinal: the [7](cardinal)   <!-- predicted: explain: the [7](cocktail) -->
    - slot{"cocktail": "7"}
    - slot{"cardinal": "7"}
    - choice_form
    - slot{"cardinal": 6}
    - slot{"category": null}
    - slot{"ingr_list": ""}
    - slot{"cardinal": null}
    - slot{"cocktail": "tuxedo cocktail"}
    - slot{"proposes": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_explanation   <!-- predicted: action_listen -->
* affirm: yes
    - action_explain
    - slot{"cocktail": "tuxedo cocktail"}
* ask_preparation: prepare it
    - action_preparation
    - slot{"cocktail": "tuxedo cocktail"}
* thanks: thank you
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* deny: i'm done
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


## Story 7 (tests/conversation_tests.md)
* search_provider: i want a drink
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "category"}
* form: search_provider: [cocktail](category)
    - form: search_form
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* explain: explain [martini](cocktail)
    - slot{"cocktail": "martini"}
    - slot{"cocktail": "martini"}
    - action_explain
    - slot{"cocktail": "martini"}
    - action_listen   <!-- predicted: utter_ask_continue -->
    - action_listen
* form: search_provider: [dry vermouth](ingredient)   <!-- predicted: search_provider: [dry vermouth](cocktail) -->
    - slot{"cocktail": "dry vermouth"}
    - search_form
    - slot{"ingredient": ["dry vermouth"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "dry vermouth"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* form: search_provider: [vodka](ingredient)
    - form: search_form
    - slot{"ingredient": ["vodka"]}
    - slot{"multiple_options": false}
    - slot{"category": "cocktail"}
    - slot{"ingredient": null}
    - slot{"ingr_list": "dry vermouth,vodka"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - search_form   <!-- predicted: action_listen -->
    - form{"name": "search_form"}
    - slot{"category": "cocktail"}
    - slot{"requested_slot": "ingredient"}
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_ask_confirm
    - slot{"ingr_list": "dry vermouth,vodka"}
* affirm: yes please
    - action_search
    - slot{"category": "cocktail"}
    - slot{"ingr_list": "dry vermouth,vodka"}
    - slot{"proposes": null}
    - slot{"more_results": false}
    - slot{"cocktail": "dirty martini"}
    - utter_ask_explanation
* affirm: yes
    - action_explain
    - slot{"cocktail": "dirty martini"}
* thanks: thank
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_you_are_welcome_ask_something_else
* deny: no more
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_reset_all_slots
    - utter_goodbye


