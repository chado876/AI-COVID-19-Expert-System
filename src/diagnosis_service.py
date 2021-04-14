from models.diagnosis import Diagnosis
import dbUtil as dbUtil
import prologUtil as prologUtil

def diagnose(firstname,lastname,age,gender,symptoms,temperature):
    diagnosis = Diagnosis()

    diagnosis.first_name = firstname
    diagnosis.last_name = lastname
    diagnosis.email = "demo@email.com"
    diagnosis.age = age
    diagnosis.symptoms = symptoms
    diagnosis.temperature = temperature
    diagnosis.total_ulhi = 3
    diagnosis.total_common = 0
    diagnosis.total_less_common = 0
    diagnosis.total_serious = 0
    diagnosis.result = "none"
    diagnosis.current_fever = False
    
    symptoms_arr = convert_symptoms_to_arr(diagnosis.symptoms)
    diagnosisResult = prologUtil.diagnose(diagnosis, symptoms_arr)

    dbUtil.add_diagnosis(diagnosis)

def convert_symptoms_to_arr(symptoms):
    print("UNFORMATTED SYMPTOMS::")
    print(symptoms)
    new_symptoms = symptoms.split(",")
    print(new_symptoms)

    symptoms_arr = [''] * 10

    print(len(new_symptoms))

    for i,x in enumerate(symptoms_arr):
        if(i < len(new_symptoms)):
            print(str(i) + " " + new_symptoms[i])
            symptoms_arr[i] = new_symptoms[i]
        else:
            symptoms_arr[i] = 'blank'
    
    print(symptoms_arr)
    return symptoms_arr

