from models.diagnosis import Diagnosis
import dbUtil as dbUtil
import prologUtil as prologUtil

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

    diagnosis.result = diagnosisResult["Result"]
    diagnosis.total_serious = diagnosisResult["TotalSerious"]
    diagnosis.total_common = diagnosisResult["TotalCommon"]
    diagnosis.total_less_common = diagnosisResult["TotalLessCommon"]
    diagnosis.current_fever = False

    results = str(diagnosis.result)
    total_serious = str(diagnosis.total_serious)
    total_common = str(diagnosis.total_common)
    total_less_common = str(diagnosis.total_less_common)
    total_ulhi = str(diagnosis.total_ulhi)

    if(diagnosis.current_fever == True):
        currentFever = "has an active fever."
    else:
        currentFever = "does not have an active fever."
    if("b'Very High Risk'") == results:
        riskVal = "Very High Risk"
    elif("b'High Risk'") == results:
        riskVal = "High Risk"
    elif("b'Low Risk'") == results:
        riskVal = "Low Risk"
    else:
        riskVal = "No Risk"

    resText = ("According to our diagnosis, patient " + diagnosis.first_name + " " + diagnosis.last_name +
    " is at a " + riskVal + " of having COVID-19. They have " + total_serious + " serious symptoms, " + total_common +
    " common symptoms, " + total_less_common + " less common symptoms, " + total_ulhi + " underlying health issues " +
    " and " + currentFever)

    dbUtil.add_diagnosis(diagnosis)    
    
    return resText

def convert_symptoms_to_arr(symptoms):
    print("UNFORMATTED SYMPTOMS::")
    print(symptoms)
    new_symptoms = symptoms.split(",")
    print(new_symptoms)

    symptoms_arr = [''] * 10

    print(len(new_symptoms))

    for i,x in enumerate(symptoms_arr):
        if(i < len(new_symptoms)):
            symptoms_arr[i] = new_symptoms[i]
        elif (x == ""):
            symptoms_arr[i] = 'blank'
        else:
            symptoms_arr[i] = 'blank'
    
    print(symptoms_arr)
    return symptoms_arr

