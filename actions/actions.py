# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet
import sqlite3

# class ActionFacilitySearch(Action):
#
#     def name(self) -> Text:
#         return "action_facility_search"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,  # 对象化tracker, 得到tracker实例
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         facility = tracker.get_slot("facility_type") # get hospital from user input.
#         address = "001 Yellow river road, Zhengzhou" # It should be retrieved from database, but for now it is just a static responses.
#         dispatcher.utter_message(text="Here is the address of the {} in {}".format(facility,address)) # 会显示在user的沟通页面上,见印度人视频.
#
#         return [SlotSet("address",address)] # 在这里手动填充address这个slot, 不用entity同名自动填充了.

# class ValidateUserForm(Action):
#
#     def name(self) -> Text:
#         return "user_details_form"
#
#     def run(
#         self,
#         dispatcher: "CollectingDispatcher",
#         tracker: Tracker,
#         domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         required_slots = ["name","number"]
#
#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 return [SlotSet("requested_slot",slot_name)]
#
#         return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):  # form is done, 使用form里的slots.
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        number = tracker.get_slot("number")
        dispatcher.utter_message(text = "thanks for providing your information. Name:{}, Mobile phone:{}.Your appointment has been made.".format(name,number))

class ActionHospitalInfo(Action):

    def name(self) -> Text:
        return "action_hospital_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        connection = sqlite3.connect('chatbot.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM hospitals")
        items = cursor.fetchall()

        list = ""

        for item in items:
            s = str(item).split('\'')
            list1 =  s[1] + ", " + s[3] + ", " + s[5] + ", " + s[7] + ", " + s[9] + '\n'
            list = list + list1

        location = tracker.get_slot("location")
        dispatcher.utter_message(text = "Here is the information of hospitals in {}".format(location) + '\n' + list)
        connection.close()

class ActionDiseaseInfo(Action):

    def name(self) -> Text:
        return "action_disease_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        connection = sqlite3.connect('chatbot.db')
        cursor = connection.cursor()

        disease = tracker.get_slot("disease")
        cursor.execute("SELECT * FROM diseases WHERE NAME = ?", (disease,))  # 看教程.
        items = cursor.fetchall()

        for item in items:
            s = str(item).split('\'')
            list = s[1] + '\n' + "causes:" + '\n' + s[3] + '\n' + "treatments:" + '\n' + s[
                5] + '\n' + "preventative measures:" + '\n' + s[7]

        dispatcher.utter_message(text = "Here are the disease causes, treatments, preventative measures of {}".format(disease) + '\n' + list)
        connection.close()

