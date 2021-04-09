
import os

def read_symptoms():
    f = open("symptoms.txt", "r")
    symptoms = f.read()
    f.close()
    return symptoms

# f = open("symptoms.txt", "r") 
# print(f.read())
# f.close()