from pyswip import Prolog
import fileUtil 
from models.diagnosis import Diagnosis

prolog = Prolog()

def assert_symptom(new_symptom,severity):
    prolog.consult("./prolog/symptoms.pl")
    new_symptom = "'{}'".format(new_symptom.rstrip())
    if (severity == "serious"):
        prolog.assertz('serious_symptoms(%s)' % new_symptom)
        print("Symptom:" + new_symptom + " asserted to" + severity + " successfully.")
        print("UPDATED FACTS - SERIOUS SYMPTOMS")
        for symptom in prolog.query("serious_symptoms(X)"):
            print(symptom["X"])
    elif (severity == "common"):
        prolog.assertz('common_symptoms(%s)' % new_symptom)
        print("Symptom:" + new_symptom + " asserted to" + severity + " successfully.")
        print("UPDATED FACTS - COMMON SYMPTOMS")
        for symptom in prolog.query("common_symptoms(X)"):
            print(symptom["X"])

    elif (severity == "less-common"):
        prolog.assertz('less_common_symptoms(%s)' % new_symptom)
        print("Symptom:" + new_symptom + " asserted to" + severity + " successfully.")
        print("UPDATED FACTS - LESS COMMON SYMPTOMS:")
        for symptom in prolog.query("less_common_symptoms(X)"):
            print(symptom["X"])

def assert_all_symptoms():
    serious_symptoms = fileUtil.read_symptoms("serious")
    common_symptoms = fileUtil.read_symptoms("common")
    less_common_symptoms = fileUtil.read_symptoms("less-common")
    prolog.consult("./prolog/diagnosis.pl")

    for symptom in serious_symptoms:
        symptom =  "'{}'".format(symptom.rstrip())
        prolog.assertz('serious_symptoms(%s)' % symptom)
        print("Symptom:" + symptom + " asserted to serious_symptoms successfully.")
    for symptom in common_symptoms:
        symptom =  "'{}'".format(symptom.rstrip())
        prolog.assertz('common_symptoms(%s)' % symptom)
        print("Symptom:" + symptom + " asserted to common_symptoms successfully.")
    for symptom in less_common_symptoms:
        symptom =  "'{}'".format(symptom.rstrip())
        prolog.assertz('less_common_symptoms(%s)' % symptom)    
        print("Symptom:" + symptom + " asserted to less_common_symptoms successfully.")



    
def diagnose(diagnosis:Diagnosis, symptoms):
    assert_all_symptoms()
    prolog.consult("./prolog/diagnosis.pl")
    query = (f"diagnose({str(diagnosis.temperature)},{str(diagnosis.age)},{str(diagnosis.total_ulhi)}," +
    f"'{symptoms[0]}','{symptoms[1]}','{symptoms[2]}','{symptoms[3]}','{symptoms[4]}','{symptoms[5]}','{symptoms[6]}'," +
    f"'{symptoms[7]}','{symptoms[8]}','{symptoms[9]}',TotalSerious,TotalCommon,TotalLessCommon,CurrentFever," +
    f"{str(diagnosis.systolic_val)},{str(diagnosis.diastolic_val)},Low_bp,Result)")
    
    print("QUERY IS:" + query)
    for soln in prolog.query(query):
        R = soln
        print 
    print(R["Result"])
    print(R["TotalSerious"])
    print(R["TotalCommon"])
    print(R["TotalLessCommon"])
    print(R["CurrentFever"])
    print(R["Low_bp"])
    
    return R

def diagnose2():
    assert_all_symptoms()
    prolog.consult("./prolog/diagnosis.pl")
    for soln in prolog.query("diagnose(96.8,24,3,'Loss of Speech','Dry Cough','Tiredness','blank','blank','blank','blank','blank','blank','blank',TotalSerious,TotalCommon,TotalLessCommon,CurrentFever,100,80,Low_bp,Result)"):
        R = soln
        print 
    print(R["Result"])
    print(R["TotalSerious"])
    print(R["TotalCommon"])
    print(R["TotalLessCommon"])
    print(R["CurrentFever"])
    print(R["Low_bp"])

diagnose2()


