from pyswip import Prolog
import fileUtil 

prolog = Prolog()

def assert_symptom():
    prolog.consult("./prolog/symptoms.pl")
    symptoms = fileUtil.read_symptoms()
    for symptom in symptoms:
        prolog.assertz('symptom(%s)' % symptom)
    for symptom in prolog.query("symptom(X)"):
        print(symptom["X"])

def assert_common_symptom():
    prolog.consult("./prolog/diagnosis.pl")
    symptoms = fileUtil.read_symptoms()
    for symptom in symptoms:
        prolog.assertz('common_symptoms(%s)' % symptom)
    for symptom in prolog.query("common_symptoms(X)"):
        print(symptom["X"])

def diagnose():
    prolog.consult("./prolog/diagnosis.pl")
    for soln in prolog.query("diagnose(100.5,34,3,fever,nausea,tiedness,ahes_and_pains,ore_throat,diarroea,conjuctiitis,headahe,loss_of_tate,ash,chest_pain,los_of_speech,Serious,Common,LessCommon,CurrentFever,Result)"):
        R = soln
        print 
    print(R["Result"])
    print(R["Serious"])
    print(R["Common"])
    print(R["LessCommon"])
    print(R["CurrentFever"])


assert_common_symptom()
diagnose()


