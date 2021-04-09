
import os

def read_symptoms():
    with open("symptoms.txt") as f:
        symptoms = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        symptoms_list = [x.strip() for x in symptoms] 
        return symptoms

