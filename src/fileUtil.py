import os
from openpyxl import Workbook
import dbUtil as dbUtil


def read_symptoms(severity):
    if (severity == "serious"):
        file_directory = 'serious_symptoms.txt'
    elif (severity == "common"):
        file_directory = 'common_symptoms.txt'
    elif (severity == "less-common"):
        file_directory = 'less_common_symptoms.txt'

    with open(file_directory) as f:
        symptoms = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        symptoms_list = [x.rstrip() for x in symptoms] 
        return symptoms

def add_symptom(symptom,severity):
    if (severity == "serious"):
        file_directory = 'serious_symptoms.txt'
    elif (severity == "common"):
        file_directory = 'common_symptoms.txt'
    elif (severity == "less-common"):
        file_directory = 'less_common_symptoms.txt'
    # Open a file with access mode 'a'
    file_object = open(file_directory, 'a')
    # Append 'hello' at the end of file
    file_object.write(symptom + "\n")
    # Close the file
    file_object.close()
    # prologUtil.assert_symptom()

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

def read_all_symptoms():
    serious = read_symptoms("serious")
    common = read_symptoms("common")
    less_common = read_symptoms("less-common")

    all_symptoms = serious + common + less_common
    all_symptoms[:] = [x for x in all_symptoms if x.strip()]
    return all_symptoms

def diagnoses_from_db_to_excel():
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Diagnoses"
    col_names = dbUtil.get_column_names() 
    diagnoses = dbUtil.get_diagnoses()
    col_count = len(col_names)
    for i,x in enumerate(col_names):
        col_names[i] = x.replace("_", " ").title()
    sheet.append(col_names)
    
    iter = 1
    for x,diagnosis in enumerate(diagnoses):
        offset = 1
        for i in range(col_count):
            print(diagnosis.first_name)
            sheet.cell(row=offset+iter,column=1).value = diagnosis.id
            sheet.cell(row=offset+iter,column=2).value = diagnosis.first_name
            sheet.cell(row=offset+iter,column=3).value = diagnosis.last_name
            sheet.cell(row=offset+iter,column=4).value = diagnosis.email
            sheet.cell(row=offset+iter,column=5).value = diagnosis.temperature
            sheet.cell(row=offset+iter,column=6).value = diagnosis.age
            sheet.cell(row=offset+iter,column=7).value = diagnosis.symptoms
            sheet.cell(row=offset+iter,column=8).value = diagnosis.total_ulhi
            sheet.cell(row=offset+iter,column=9).value = diagnosis.total_serious
            sheet.cell(row=offset+iter,column=10).value = diagnosis.total_common
            sheet.cell(row=offset+iter,column=11).value = diagnosis.total_less_common
            sheet.cell(row=offset+iter,column=12).value = diagnosis.systolic_val
            sheet.cell(row=offset+iter,column=13).value = diagnosis.diastolic_val
            sheet.cell(row=offset+iter,column=14).value = diagnosis.low_bp
            sheet.cell(row=offset+iter,column=15).value = diagnosis.current_fever
            sheet.cell(row=offset+iter,column=16).value = diagnosis.result

        iter = iter + 1

    workbook.save("data/diagnoses.xlsx")


