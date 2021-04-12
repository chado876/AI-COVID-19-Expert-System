from pyswip import Prolog
import fileUtil as fileUtil

def assert_symptom():
    prolog = Prolog()
    prolog.consult("./prolog/symptoms.pl")
    symptoms = fileUtil.read_symptoms()
    for symptom in symptoms:
        prolog.assertz('symptom(%s)' % symptom)
    for symptom in prolog.query("symptom(X)"):
        print(symptom["X"])




