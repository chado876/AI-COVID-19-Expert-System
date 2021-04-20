import eel
import random
from datetime import datetime
import fileUtil as fileUtil
import diagnosis_service as diagnosis_service
import dbUtil as dbUtil
import prologUtil as prologUtil
import email_service as email_service
import time
import alert_service as alert_service

eel.init('web')

@eel.expose
def diagnose(firstname,lastname,email,age,symptoms,ulhi,temperature):
    symptoms = [x.replace('\n', '') for x in symptoms]
    symptoms = ','.join(symptoms) #convert list of symptoms to single string seperated by commas
    print("DIAGNOSIS DETAILS::" + firstname + lastname + age  + symptoms + str(temperature))
    result = diagnosis_service.diagnose(firstname,lastname,email,age,symptoms,ulhi,temperature)
    print("FINAL DIAGNOSIS:::")
    print(result)
    newResultText = (result + "\n An email has been sent to the patient with these results as well as" +
    " short-term and long-term precautions to take going forward.")
    time.sleep(3)
    eel.showResult(newResultText) 
    email_diagnosis(email,result)

@eel.expose
def get_symptoms():
    symptoms = fileUtil.read_all_symptoms()
    print("SYMPTOMS::", symptoms)
    eel.add_symptom_checkboxes(symptoms)

@eel.expose
def get_ulhi():
    ulhi = fileUtil.read_ulhi()
    eel.createUlhiCheckboxes(ulhi)

@eel.expose
def assert_all_symptoms_from_txt():
    prologUtil.assert_all_symptoms()

@eel.expose
def add_symptom(symptom,severity):
    fileUtil.add_symptom(symptom,severity)
    # prologUtil.assert_symptom(symptom,severity)
    
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

@eel.expose
def email_all_diagnoses():
    fileUtil.diagnoses_from_db_to_excel() #generate spreadsheet
    email_service.send_diagnoses_report()

@eel.expose
def email_diagnosis(email, resultText):
    email_service.send_diagnosis(email,resultText)

@eel.expose
def delete_symptoms(symptoms):
    fileUtil.delete_symptoms(symptoms)

@eel.expose
def init_alerts():
    alert_service.init_alerts()

@eel.expose 
def update_alert(alert_type,val):
    alert_service.update_alert(alert_type,val)

@eel.expose
def get_alert_vals():
    vals = alert_service.get_alert_vals()
    eel.setAlertVals(vals) 

@eel.expose
def get_statistics():
    total = dbUtil.count_total_diagnoses()
    veryhigh_results = dbUtil.query_db("Very High Risk") 
    total_veryhigh = len(veryhigh_results)
    high_results = dbUtil.query_db("High Risk")
    total_high = len(high_results)
    lowrisk_results = dbUtil.query_db("Low Risk")
    total_low = len(lowrisk_results) 
    norisk_results = dbUtil.query_db("Not at Risk")
    total_norisk = len(norisk_results) 

    eel.getStatValues(total,total_veryhigh,total_high,total_low,total_norisk)

    
@eel.expose
def get_ulhi_and_symptoms():
    symptoms = fileUtil.read_all_symptoms()
    ulhi = fileUtil.read_ulhi()
    values = symptoms + ulhi
    print(values)
    eel.createUlhiAndSymptomsCheckboxes(values) 

@eel.expose
def reset_db():
    dbUtil.drop_diagnoses()
    
eel.start('index.html',size=(700,480)),
