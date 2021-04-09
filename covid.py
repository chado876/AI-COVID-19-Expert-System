import eel
import random
from datetime import datetime
from utils.fileUtil import read_symptoms

eel.init('web')

@eel.expose
def get_symptoms():
    symptoms = read_symptoms()
    print("SYMPTOMS::", symptoms)
    eel.add_symptom_checkboxes(symptoms)
    
@eel.expose
def get_random_name():
    eel.prompt_alerts('Random name')

@eel.expose
def get_random_number():
    eel.prompt_alerts(random.randint(1, 100))

@eel.expose
def get_date():
    eel.prompt_alerts(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

@eel.expose
def get_ip():
    eel.prompt_alerts('127.0.0.1')
    

eel.start('index.html',size=(700,480)),