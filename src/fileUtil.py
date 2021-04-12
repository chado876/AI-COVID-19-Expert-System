import os
import prologUtil as prologUtil

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
    prologUtil.assert_symptom()

def update_stats(stat):
    # total - total diagnoses, high - high risk, low- low risk
    if(stat == "total"):
        a_file = open("stats.txt", "r")
        list_of_lines = a_file. readlines()
        current_stats = list_of_lines
        current_stats[0] = str(int(current_stats[0]) + 1) + "\n"
        a_file = open("stats.txt", "w")
        a_file.writelines(current_stats)
        a_file.close()
    # elif(stats == "high"):
    #     # do something
    # elif(stats == "low"):
    #         # do something

def read_stats():
    with open("stats.txt") as f:
        stats = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        stats_list = [x.strip() for x in stats] 
        print(stats_list)
        return stats_list

   

