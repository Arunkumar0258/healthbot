from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

import logging
import rasa_core
import os
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.facebook import FacebookInput
from bot_server_channel import BotServerInputChannel
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core import config

logger = logging.getLogger(__name__)

def train_dialouge(domain_file='domain.yml',
                   output_model_path='./models/dialogue',
                   training_data_file='./data/stories.md'):

    fallback = FallbackPolicy(fallback_action_name='action_default_fallback',
                              core_threshold = 0.3,
                              nlu_threshold=0.1)

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(),
                            KerasPolicy(max_history=3, epochs=50, batch_size=2),
                            fallback])
    data = agent.load_data(training_data_file)
    agent.train(data)
    agent.persist(output_model_path)

    return agent

def run_health_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/default/healthbot')
    action_endpoint = EndpointConfig(url='http://localhost:5055/webhook')
    agent = Agent.load('./models/dialogue', interpreter=interpreter,
                       action_endpoint=action_endpoint)

    channel = BotServerInputChannel(agent, port=5002)

    input_channel = FacebookInput(
        fb_verify=os.environ['FB_VERIFY'],
        fb_secret=os.environ['FB_BOT_SECRET'],
        fb_access_token=os.environ['FB_PAGE_ACCESS_TOKEN']
    )
    agent.handle_channels([channel, input_channel], http_port=5002, serve_forever=True)
    #  rasa_core.run.serve_application(agent, channel=s, credentials_file='./credentials.yml')

if __name__ == '__main__':
    train_dialouge()
    run_health_bot()
