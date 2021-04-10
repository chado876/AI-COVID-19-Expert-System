
import os

def read_symptoms():
    with open("symptoms.txt") as f:
        symptoms = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        symptoms_list = [x.strip() for x in symptoms] 
        return symptoms

def add_symptom(symptom):
    # Open a file with access mode 'a'
    file_object = open('symptoms.txt', 'a')
    # Append 'hello' at the end of file
    file_object.write(symptom + "\n")
    # Close the file
    file_object.close()

