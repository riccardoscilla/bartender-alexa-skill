# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, ActionExecutionRejection
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset
from rasa_sdk.forms import FormAction, REQUESTED_SLOT

import pandas as pd
import random

class Data:
    def __init__(self):
        self.df = pd.read_excel('../data/data.xlsx')
        self.ingr = self.get_ingr()
        self.cat = self.get_cat()

    def get_ingr(self):
        ingr = []
        for index, row in self.df.iterrows():
            r = row["Ingredients"].split(',')
            for i in r:
                if i.lower() not in ingr:
                    ingr.append(i.lower())
        return ingr

    def get_cat(self):
        cat = []
        for index, row in self.df.iterrows():
            r = row["Category"].split(',')
            for i in r:
                if i.lower() not in cat:
                    cat.append(i.lower())
        return cat


class SearchForm(FormAction):
    def name(self):
        return "search_form"

    @staticmethod
    def required_slots(tracker):
        return ["category","ingredient"]

    def request_next_slot(self, dispatcher, tracker, domain):

        multiple_options = tracker.get_slot("multiple_options")
        for slot in self.required_slots(tracker):
            if slot == "category":
                if self._should_request_slot(tracker, slot):
                    dispatcher.utter_message(template=f"utter_ask_{slot}", **tracker.slots)
                    return [SlotSet(REQUESTED_SLOT, slot)]
            elif slot == "ingredient":
                if self._should_request_slot(tracker, slot):
                    ingr_list = tracker.get_slot("ingr_list")
                    if isinstance(ingr_list,str):
                        ingr_list = tracker.get_slot("ingr_list").split(',')
                        if '' in ingr_list: ingr_list.remove('')
                    if len(ingr_list) == 0:
                        if not multiple_options:
                            dispatcher.utter_message(template=f"utter_ask_{slot}", **tracker.slots)
                    else:
                        if not multiple_options:
                            dispatcher.utter_message(template=f"utter_ask_more_{slot}", **tracker.slots)
                    return [SlotSet(REQUESTED_SLOT, slot)]
        return None

    def submit(self,dispatcher,tracker,domain):
        cat = tracker.get_slot("category")
        ingr_valid = [i.lower() for i in tracker.get_slot("ingredient")]
        ingr_list = tracker.get_slot("ingr_list")
        multiple_options = tracker.get_slot("multiple_options")
        if isinstance(ingr_list,list):
            ingr_list = ','.join(ingr_list)
        for ingr in ingr_valid:
            if len(ingr_list) > 0:
                ingr_list += ","
            ingr_list += ingr

        return [SlotSet("category", cat), 
                SlotSet("ingredient", None), 
                SlotSet("ingr_list", ingr_list)]

    def validate_category(self,value,dispatcher,tracker,domain):
        cat = value.lower()
        if cat in Data().cat:
            return {"category": cat}
        else:
            dispatcher.utter_message(text="Sorry I don't {} drinks".format(cat))
            dispatcher.utter_message(template="utter_list_category")
            return {"category": None}

    def validate_ingredient(self,value,dispatcher,tracker,domain):
        if not isinstance(value,list):
            value = [value.lower()]
        ingr_choice = [v.lower() for v in value]

        cat = tracker.get_slot("category")
        ingr_list = tracker.get_slot("ingr_list")
        multiple_options_slot = tracker.get_slot("multiple_options")
        if isinstance(ingr_list,str):
            ingr_list = tracker.get_slot("ingr_list").split(',')
            if '' in ingr_list: ingr_list.remove('')

        ingr_valid = None
        multiple_options = False
        utter_affirm = True

        for ingr in ingr_choice:

            options = []        
            for i in Data().ingr:
                if len(ingr.split())>1:
                    if ingr in i:
                        options.append(i)
                else:
                    if ingr in i.split():
                        options.append(i)

            if len(options) > 0:
                if ingr_valid is None:
                    ingr_valid = []

                if len(options) > 1 and not multiple_options_slot:
                    multiple_options = True
                    txt = "I know multiple {}:\n".format(ingr)
                    for mo in options:
                        txt += "{}.\n".format(mo.capitalize())
                    txt += "Which one do you want?"
                    dispatcher.utter_message(text=txt)
                    utter_affirm = False
                else:
                    if ingr not in ingr_list:
                        ingr_valid.append(ingr)
                        #utter_affirm += 1
                    else:
                        dispatcher.utter_message(text="You already have {} in you list".format(ingr.capitalize()))
                        utter_affirm = False
            else:
                dispatcher.utter_message(text="Sorry I don't know {} with {}".format(cat if cat else "drink",ingr.capitalize()))
                utter_affirm = False

        if utter_affirm and cat != None:
            dispatcher.utter_message(template="utter_affirm")
        return {"ingredient": ingr_valid, "multiple_options": multiple_options}


class ActionAskConfirm(Action):
    def name(self):
        return "action_ask_confirm"

    def run(self,dispatcher,tracker,domain):
        ingr_list = tracker.get_slot("ingr_list")
        cat = tracker.get_slot("category")
        if isinstance(ingr_list,str):
            ingr_str = ingr_list
            ingr_list = tracker.get_slot("ingr_list").split(',')
            if '' in ingr_list: ingr_list.remove('')

        if len(ingr_list) == 0:
            dispatcher.utter_message(text="Ops your ingredient list is empty.")
            dispatcher.utter_message(template=f"utter_ask_something_else")
            return [SlotSet("ingr_list", '')]
        else:
            res = ''
            for i in range(len(ingr_list)):
                if i == len(ingr_list)-1 and i != 0:
                    res+=' and '
                elif i > 0:
                    res+=', '
                res += ingr_list[i].capitalize()
            dispatcher.utter_message(text="Searching for a {} with {}. Ok?".format(cat,res))
            return [SlotSet("ingr_list", ingr_str)]

class ActionListIngredients(Action):
    def name(self):
        return "action_list_ingredients"

    def run(self,dispatcher,tracker,domain):
        ingr_list = tracker.get_slot("ingr_list")
        if isinstance(ingr_list,str):
            ingr_str = tracker.get_slot("ingr_list")
            ingr_list = tracker.get_slot("ingr_list").split(',')
            if '' in ingr_list: ingr_list.remove('')

        if len(ingr_list) == 0:
            dispatcher.utter_message(text="Ops your ingredient list is empty.")
            return [SlotSet("ingr_list", '')]
        else:
            res = ''
            for i in range(len(ingr_list)):
                if i == len(ingr_list)-1 and i != 0:
                    res+=' and '
                elif i > 0:
                    res+=', '
                res += ingr_list[i].capitalize()
            dispatcher.utter_message(text="You choose: {}.".format(res))
            return [SlotSet("ingr_list", ingr_str)]


class ActionSearch(Action):
    def name(self):
        return "action_search"

    def run(self,dispatcher,tracker,domain):
        cat = tracker.get_slot("category")
        ingr_list = tracker.get_slot("ingr_list")

        prev_prop = tracker.get_slot("proposes")
        prop = '' if prev_prop == None else prev_prop 
        prev_prop = [] if prev_prop == None else prev_prop.split(',')

        if isinstance(ingr_list,str):
            ingr_str = tracker.get_slot("ingr_list")
            ingr_list = tracker.get_slot("ingr_list").split(',')
            if '' in ingr_list: ingr_list.remove('')

        if len(ingr_list) == 0:
            dispatcher.utter_message(text="Ops your ingredient list is empty.")
            dispatcher.utter_message(template=f"utter_ask_something_else")
            return [SlotSet("category", None),
                    SlotSet("ingr_list", ''),
                    SlotSet("proposes", None)]

        proposes = []

        for index, row in Data().df.iterrows():
            if all(ingr in row["Ingredients"].split(',') for ingr in ingr_list) \
                and cat==row["Category"]:
                proposes.append(row["Name"])

        if prev_prop != None:
            proposes = [x for x in proposes if x not in prev_prop]
        idx_init = len(prev_prop)+1 if prev_prop != None else 1

        if len(proposes) > 1:
            res = ''
            if len(proposes) >= 3:
                for i in range(3):
                    cocktail = proposes.pop(random.randint(0,len(proposes)-1))
                    res += '\n{}. {}.'.format(idx_init,cocktail.capitalize())
                    idx_init += 1
                    prop += (',' if prev_prop != [] and i == 0 else '')
                    prop += cocktail+','
            else:
                for i in range(len(proposes)):
                    cocktail = proposes.pop(random.randint(0,len(proposes)-1))
                    res += '\n{}. {}.'.format(idx_init,cocktail.capitalize())
                    idx_init += 1
                    prop += (',' if prev_prop != [] and i == 0 else '')
                    prop += cocktail+','
            dispatcher.utter_message(text="You can drink: {}".format(res))
            if len(proposes) > 0:
                dispatcher.utter_message(text="Do you want to see more results?")
                return [SlotSet("category", cat), 
                        SlotSet("ingr_list", ingr_str),
                        SlotSet("proposes", prop[:-1]),
                        SlotSet("more_results", True),
                        SlotSet("cocktail", None)]
            else:
                return [SlotSet("category", cat), 
                        SlotSet("ingr_list", ingr_str),
                        SlotSet("proposes", prop[:-1]),
                        SlotSet("more_results", False),
                        SlotSet("cocktail", None)]

        if len(proposes) == 1:
            cocktail = proposes.pop(random.randint(0,len(proposes)-1))
            dispatcher.utter_message(text="You can drink: {}".format(cocktail.capitalize()))
            return [SlotSet("category", cat), 
                        SlotSet("ingr_list", ingr_str),
                        SlotSet("proposes", None),
                        SlotSet("more_results", False),
                        SlotSet("cocktail", cocktail)]      
        else: 
            res = ''
            for i in range(len(ingr_list)):
                if i == len(ingr_list)-1 and i != 0:
                    res+=' and '
                elif i > 0:
                    res+=', '
                res += ingr_list[i].capitalize()
            dispatcher.utter_message(text="Sorry we don't have any {} with {}.".format(cat,res))
            return [SlotSet("category", None), 
                    SlotSet("ingr_list", ''), 
                    SlotSet("proposes", None),
                    SlotSet("more_results", False),
                    SlotSet("cocktail", None)]



class ChoiceForm(FormAction):
    def name(self):
        return "choice_form"

    @staticmethod
    def required_slots(tracker):
        return ["cardinal"]

    def request_next_slot(self, dispatcher, tracker, domain):
        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):
                dispatcher.utter_message(template=f"utter_ask_{slot}", **tracker.slots)
                return [SlotSet(REQUESTED_SLOT, slot)]
        return None

    def submit(self,dispatcher,tracker,domain):
        cardinal = tracker.get_slot("cardinal")
        proposes = tracker.get_slot("proposes").split(',')
        cocktail = proposes[cardinal]
        dispatcher.utter_message(text="{}, Nice choice!".format(cocktail.capitalize()))
        return [SlotSet("category",None), 
                SlotSet("ingr_list", ''),
                SlotSet("cardinal",None), 
                SlotSet("cocktail",cocktail), 
                SlotSet("proposes",None)]

    def validate_cardinal(self,value,dispatcher,tracker,domain):
        proposes = tracker.get_slot("proposes").split(',')
        value = int(value) -1
        if value < len(proposes):
            return {"cardinal": value}
        else:
            dispatcher.utter_message(text="This value is not in the list")
            return {"cardinal": None}

class ActionExplain(Action):
    def name(self):
        return "action_explain"

    def run(self,dispatcher,tracker,domain):
        cocktail = tracker.get_slot("cocktail")

        if cocktail == None:
            dispatcher.utter_message(text="Ops you didn't specifiy the cocktail.")
            dispatcher.utter_message(template=f"utter_ask_something_else")
            return [SlotSet("cocktail", None)]

        category, alcoholic, ingredients = None, None, None
        for index, row in Data().df.iterrows():
            if cocktail == row["Name"]:
                category = row["Category"]
                alcoholic = row["Alcoholic"]
                ingredients = row["Ingredients"].split(',')
                image = row["Img"]

        if category is not None and alcoholic is not None and ingredients is not None and image is not None:
            res = ''
            for i in range(len(ingredients)):
                if i == len(ingredients)-1 and i != 0:
                    res+=' and '
                elif i > 0:
                    res+=', '
                res += ingredients[i].capitalize()
            dispatcher.utter_message(text="{} is an {} {} made with {}.".format(cocktail.capitalize(),alcoholic,category,res))
            #print(image)
            #dispatcher.utter_attachment(attachment=image)
            #dispatcher.utter_message(image="https://www.thecocktaildb.com/images/media/drink/qgdu971561574065.jpg")
            return [SlotSet("cocktail", cocktail)]

        else:
            dispatcher.utter_message(text="Sorry I don't know {}".format(cocktail))
            return [SlotSet("cocktail", None)]

class ActionPreparation(Action):
    def name(self):
        return "action_preparation"

    def run(self,dispatcher,tracker,domain):
        cocktail = tracker.get_slot("cocktail")
        if cocktail == None:
            dispatcher.utter_message(text="Ops you didn't specifiy the cocktail.")
            dispatcher.utter_message(template=f"utter_ask_something_else")
            return [SlotSet("cocktail", None)]

        glass, ingredients, measures, instructions = None, None, None, None
        for index, row in Data().df.iterrows():
            if cocktail == row["Name"]:
                glass = row["Glass"]
                ingredients = row["Ingredients"].split(',')
                measures = row["Measures"].split(',')
                instructions = row["Instructions"]

        if glass is not None and ingredients is not None and measures is not None:
            txt = 'For {} you need {}.\n'.format(cocktail.capitalize(),glass)
            txt += 'Here are the ingredients:\n'
            for i in range(len(ingredients)):
                txt += '{}; {}.\n'.format(measures[i],ingredients[i].capitalize())           
            if instructions is not None:
                txt += 'Instructions:\n{}'.format(instructions)
            dispatcher.utter_message(text="{}".format(txt))   
            return [SlotSet("cocktail", cocktail)]
        else:
            dispatcher.utter_message(text="Sorry I don't know {}".format(cocktail.capitalize()))
            dispatcher.utter_message(template=f"utter_ask_something_else")
            return [SlotSet("cocktail", None)]


class ActionRepeateMessage(Action):
    def name(self):
        return "action_repeat"

    def run(self, dispatcher, tracker, domain):
        user_ignore_count = 2
        count = 0
        tracker_list = []

        while user_ignore_count > 0:
            event = tracker.events[count].get('event')
            if event == 'user':
                user_ignore_count = user_ignore_count - 1
            if event == 'bot':
                tracker_list.append(tracker.events[count])
            count = count - 1

        for i in reversed(range(len(tracker_list))):
            data = tracker_list[i].get('data')
            image = data['image'] if data['image'] is not None else None
            if data:
                if not image:
                    dispatcher.utter_message(text=tracker_list[i].get('text'))
                else:
                    dispatcher.utter_message(image=image)
        return []


class ActionRepeateMessageContinue(Action):
    def name(self):
        return "action_continue"

    def run(self, dispatcher, tracker, domain):
        user_ignore_count = 2
        count = 0
        tracker_list = []

        while user_ignore_count > 0:
            event = tracker.events[count].get('event')
            if event == 'user':
                user_ignore_count = user_ignore_count - 1
            if event == 'bot':
                tracker_list.append(tracker.events[count])
            count = count - 1

        for i in range(len(tracker_list)):
            data = tracker_list[i].get('data')
            if data:
                if tracker_list[i].get('text') == "Do you want to see more results?" \
                    or tracker_list[i].get('text') == "Which one do you want?":
                    dispatcher.utter_message(text=tracker_list[i].get('text'))
        return []


class ActionResetAllSlots(Action):
    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]