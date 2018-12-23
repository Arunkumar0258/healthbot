from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import os
import infermedica_api

class ActionMed(Action):
    def name(self):
        return 'action_medicine'

    def run(self, dispatcher, tracker, domain):
        api = infermedica_api.API(app_id=os.environ['APP_ID'],
                                  app_key=os.environ['API_KEY'])

        symp = tracker.get_slot('symptom')
        request = infermedica_api.Diagnosis(sex='male', age='25')

        symp = api.parse(symp).to_dict()
        symp_id = symp['mentions'][0]['id']
        request.add_symptom(symp_id, 'present')

        request = api.diagnosis(request)

        response = request.question.text
        #  response = "Let's try this medicine"

        dispatcher.utter_message(response)
        return [SlotSet('symptom', symp)]

