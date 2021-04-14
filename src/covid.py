import eel
import random
from datetime import datetime
import fileUtil as fileUtil
import diagnosis_service as diagnosis_service
import dbUtil as dbUtil
import prologUtil as prologUtil

eel.init('web')

@eel.expose
def diagnose(firstname,lastname,age,gender,symptoms,temperature):
    symptoms = [x.replace('\n', '') for x in symptoms]
    symptoms = ','.join(symptoms) #convert list of symptoms to single string seperated by commas
    print("DIAGNOSIS DETAILS::" + firstname + lastname + age + gender + symptoms + str(temperature))
    diagnosis_service.diagnose(firstname,lastname,age,gender,symptoms,temperature)

@eel.expose
def get_symptoms():
    symptoms = fileUtil.read_all_symptoms()
    print("SYMPTOMS::", symptoms)
    eel.add_symptom_checkboxes(symptoms)

@eel.expose
def assert_all_symptoms_from_txt():
    prologUtil.assert_all_symptoms()

@eel.expose
def add_symptom(symptom,severity):
    fileUtil.add_symptom(symptom,severity)
    prologUtil.assert_symptom(symptom,severity)
    

@eel.expose
def update_stats(stat): 
    fileUtil.update_stats(stat)

@eel.expose
def read_stats():
    stats = fileUtil.read_stats()
    print("STATS::", stats)
    eel.addStats(stats)

@eel.expose 
def get_total_diagnoses():
    total = dbUtil.count_total_diagnoses()
    eel.addStats(total)

    

eel.start('index.html',size=(700,480)),