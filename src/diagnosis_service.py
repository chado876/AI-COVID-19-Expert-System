from models.diagnosis import Diagnosis
from models.alert import Alert
import dbUtil as dbUtil
import prologUtil as prologUtil
import email_service as email_service
import fileUtil as fileUtil
import alert_service as alert_service

def diagnose(firstname,lastname,email,age,symptoms,ulhi,temperature):
    diagnosis = Diagnosis()

    ulhi_str = [x.replace('\n', '') for x in ulhi]
    ulhi_str = ','.join(ulhi) #convert list of ulhi to single string seperated by commas

    diagnosis.first_name = firstname
    diagnosis.last_name = lastname
    diagnosis.email = email
    diagnosis.age = age
    diagnosis.symptoms = symptoms
    diagnosis.underlying_health_issues = ulhi_str
    diagnosis.temperature = temperature
    diagnosis.total_ulhi = len(ulhi)
    diagnosis.total_common = 0
    diagnosis.total_less_common = 0
    diagnosis.total_serious = 0
    diagnosis.diastolic_val = 0
    diagnosis.systolic_val = 0
    diagnosis.low_bp = False
    diagnosis.current_fever = False
    diagnosis.result = "none"
    
    symptoms_arr = convert_symptoms_to_arr(diagnosis.symptoms)
    diagnosisResult = prologUtil.diagnose(diagnosis, symptoms_arr)
    
    encoding = 'utf-8' #pyswip returns results with utf-8 encoding
    diagnosis.result = diagnosisResult["Result"].decode(encoding) 
    diagnosis.total_serious = diagnosisResult["TotalSerious"]
    diagnosis.total_common = diagnosisResult["TotalCommon"]
    diagnosis.total_less_common = diagnosisResult["TotalLessCommon"]
    diagnosis.current_fever = False
    
    results = diagnosis.result
    total_serious = diagnosis.total_serious
    total_common = diagnosis.total_common
    total_less_common = diagnosis.total_less_common
    total_ulhi = diagnosis.total_ulhi

    if(diagnosis.current_fever == True):
        currentFever = "has an active fever."
    else:
        currentFever = "does not have an active fever."
    if("Very High Risk") == results:
        riskVal = "Very High Risk"
    elif("High Risk") == results:
        riskVal = "High Risk"
    elif("Low Risk") == results:
        riskVal = "Low Risk"
    else:
        riskVal = "No Risk"

    resText = ("According to our diagnosis, patient " + diagnosis.first_name + " " + diagnosis.last_name +
    " is at a " + riskVal + " of having COVID-19. They have " + str(total_serious) + " serious symptoms, " + str(total_common) +
    " common symptoms, " + str(total_less_common) + " less common symptoms, " + str(total_ulhi) + " underlying health issues " +
    " and " + currentFever)

    dbUtil.add_diagnosis(diagnosis)   

    check_for_spike()
    return resText

def convert_symptoms_to_arr(symptoms):
    new_symptoms = symptoms.split(",")
    symptoms_arr = [''] * 10 #use an array of size 10 because the prolog function is expecting 10 symptoms

    print(len(new_symptoms))

    for i,x in enumerate(symptoms_arr):
        if(i < len(new_symptoms)):
            symptoms_arr[i] = new_symptoms[i]
        elif (x == ""): #if diagnosis symptom is an empty string or if they are less than 10, pad the array
                        #size with array elements 'blank' until the array size (10) is met.
            symptoms_arr[i] = 'blank'
        else:
            symptoms_arr[i] = 'blank'
    
    print(symptoms_arr)
    return symptoms_arr

def check_for_spike():
    alerts = alert_service.get_alerts()
    very_high_risk_diagnoses = dbUtil.query_db("Very High Risk")
    high_risk_diagnoses = dbUtil.query_db("High Risk")
    low_risk_diagnoses = dbUtil.query_db("Low Risk")
    no_risk_diagnoses = dbUtil.query_db("Not at Risk")

    totVhr = len(very_high_risk_diagnoses)
    totHr = len(high_risk_diagnoses)
    totLr = len(low_risk_diagnoses)
    totNr = len(no_risk_diagnoses)

    sendAlert = False
    #check alert value stored if current diagnoses matches condition, if so, send alert email
    for alert in alerts:
        if (alert.value > 0):
            if (alert.alert_type == "Very High Risk"):
                if (totVhr >= alert.value):
                    sendAlert = True
            elif (alert.alert_type == "High Risk"):
                if (totHr >= alert.value):
                    sendAlert = True
            elif (alert.alert_type == "Low Risk"):
                if(totLr >= alert.value):
                    sendAlert = True
            elif (alert.alert_type == "Not at Risk"):
                if (totNr >= alert.value):
                    sendAlert = True
                    
    if sendAlert == True:
        fileUtil.diagnoses_from_db_to_excel() #generate spreadsheet
        email_service.send_alert(totVhr,totHr,totLr,totNr)
