from pyswip import Prolog
import fileUtil 

prolog = Prolog()

def assert_symptom(new_symptom,severity):
    prolog.consult("./prolog/symptoms.pl")
    new_symptom = new_symptom.replace(" ", "_").lower()
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
    
def diagnose():
    prolog.consult("./prolog/diagnosis.pl")
    for soln in prolog.query("diagnose(100.5,34,3,nausea,tiredness,aches,sore_throat,diarroea,conjuctivitis,headache,loss_of_taste,chest_pain,loss_of_speech,TotalSerious,TotalCommon,TotalLessCommon,CurrentFever,Result)"):
        R = soln
        print 
    print(R["Result"])
    print(R["TotalSerious"])
    print(R["TotalCommon"])
    print(R["TotalLessCommon"])
    print(R["CurrentFever"])

diagnose()


