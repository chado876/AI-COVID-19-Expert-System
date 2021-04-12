import eel
import random
from datetime import datetime
import fileUtil as fileUtil
import diagnosis_service as diagnosis_service

eel.init('web')

@eel.expose
def diagnose(firstname,lastname,age,gender,symptoms,temperature):
    symptoms = ','.join(symptoms) #convert list of symptoms to single string seperated by commas
    print("DIAGNOSIS DETAILS::" + firstname + lastname + age + gender + symptoms + temperature)
    diagnosis_service.diagnose(firstname,lastname,age,gender,symptoms,temperature)

@eel.expose
def get_symptoms():
    symptoms = fileUtil.read_symptoms()
    print("SYMPTOMS::", symptoms)
    eel.add_symptom_checkboxes(symptoms)
    
@eel.expose
def add_symptom(symptom):
    fileUtil.add_symptom(symptom) 

@eel.expose
def update_stats(stat): 
    fileUtil.update_stats(stat)

@eel.expose
def read_stats():
    stats = fileUtil.read_stats()
    print("STATS::", stats)
    eel.addStats(stats)

    

eel.start('index.html',size=(700,480)),