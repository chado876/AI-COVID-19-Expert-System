import eel
import random
from datetime import datetime
import utils.fileUtil as fileUtil

eel.init('web')

@eel.expose
def get_symptoms():
    symptoms = fileUtil.read_symptoms()
    print("SYMPTOMS::", symptoms)
    eel.add_symptom_checkboxes(symptoms)
    
@eel.expose
def add_symptom(symptom):
    fileUtil.add_symptom(symptom)
    

eel.start('index.html',size=(700,480)),