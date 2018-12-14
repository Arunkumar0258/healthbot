from rasa_nlu.training_data import  load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config

training_data = load_data('./data/nlu_data.md')
trainer = Trainer(config.load('./nlu_config.yml'))
trainer.train(training_data)

model_dir = trainer.persist('./models/', fixed_model_name='healthbot')
