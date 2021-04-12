from models.diagnosis import Diagnosis
import dbUtil as dbUtil

def diagnose(firstname,lastname,age,gender,symptoms,temperature):
    diagnosis = Diagnosis()

    diagnosis.first_name = firstname
    diagnosis.first_name = lastname
    diagnosis.email = "demo@email.com"
    diagnosis.age = age
    diagnosis.gender = gender
    diagnosis.symptoms = symptoms
    diagnosis.temperature = temperature

    dbUtil.add_diagnosis(diagnosis)

