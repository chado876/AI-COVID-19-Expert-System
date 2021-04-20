import email, smtplib, ssl
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import time


def send_diagnoses_report():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%B %d, %Y")
    currentTime = datetime.now()
    if currentTime.hour < 12 :
        greeting = ('Good morning,')
    elif 12 <= currentTime.hour < 18 :
        greeting = ('Good afternoon,')
    else :
        greeting = ('Good evening,')
    
    currentTime = str(time.strftime('%I:%M %p'))
    subject = "COVID-19 Diagnoses - " + dt_string
    body = greeting + " please see attached for a spreadsheet containing diagnoses as of " + dt_string + " at " + currentTime + "."
    sender_email = "utechmohexpertsystem2021@gmail.com"
    receiver_email = "utechmohexpertsystem2021@gmail.com"
    password = "Password@15"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "data/diagnoses.xlsx"  # In same directory as script
    filenameWithoutDir =os.path.basename(filename)

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filenameWithoutDir}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

def send_diagnosis(email,resultText):
    resultText = resultText.replace('<strong>','')
    resultText = resultText.replace('</strong>','')

    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%B %d, %Y")

    currentTime = datetime.now()
    if currentTime.hour < 12 :
        greeting = ('Good morning,')
    elif 12 <= currentTime.hour < 18 :
        greeting = ('Good afternoon,')
    else :
        greeting = ('Good evening,')
    
    currentTime = str(time.strftime('%I:%M %p'))
    if "No Risk" in resultText: 
        action = ("To avoid contracting COVID-19:\n"  
        + "1. Clean your hands often. Use soap and water, or an alcohol-based hand rub.\n" 
        + "2. Maintain a safe distance from anyone who is coughing or sneezing.\n"
        + "3. Wear a mask when physical distancing is not possible.\n"
        + "4. Don’t touch your eyes, nose or mouth.\n"
        + "5. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n"
        + "6. Stay home if you feel unwell.\n"
        + "7. If you have a fever, cough and difficulty breathing, seek medical attention.\n\n"
        + "8. You may visit this link for further information.\n" 
        + "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public?gclid=Cj0KCQjwse-DBhC7ARIsAI8YcWLN3oNoK4jl-YcEc3Q77HQhlkEeDPmMtv1wzGSHCcbEJHfCuNnH54IaAtG2EALw_wcB")
    elif "High Risk" in resultText: 
        action = ("Precautions for people with high risk of COVID-19: \n"
        + "1. Plan ahead with your doctor on when to seek routine care and what to do if you were to get sick. \n" 
        + "2. Make sure all your vaccinations are up to date.\n"
        + "3. Have sufficient quantity of your regular medication, non-perishable food and other supplies to minimize trips outside your home. \n"
        + "4. Limit in-home services and visitors to what is essential- only people that are healthy should visit.\n"
        + "5. Keep up to date on national public health advice. \n"
        + "6. Isolate yourself from any house member and outsiders for atleast 14 days")
    elif "Low Risk" in resultText: 
        action = ("Precautions for people with low risk of COVID-19: \n"
        + "1. Call your health care provider or COVID-19 hotline at 888-ONE-LOVE (663-5683) to find out where and when to get a test. \n"
        + "2. Cooperate with contact-tracing procedures to stop the spread of the virus (If Applicable). \n"
        + "3. If testing is not available, stay home and away from others for 14 days. \n"
        + "4. While you are in quarantine, do not go to work, to school or to public places. Ask someone to bring you supplies. \n"
        + "5. Keep at least a 1-metre distance from others, even from your family members. \n"
        + "6. Wear a medical mask to protect others, including if/when you need to seek medical care. \n"
        + "7. Clean your hands frequently. \n"
        + "8. Stay in a separate room from other family members, and if not possible, wear a medical mask. \n"
        + "9. Keep the room well-ventilated. \n"
        + "10. If you share a room, place beds at least 1 metre apart. \n"
        + "11. Monitor yourself for any symptoms for 14 days. \n"
        + "12. Call your health care provider immediately if you have any of these danger signs: difficulty breathing, loss of speech or mobility, confusion or chest pain. \n"
        + "13. Stay positive by keeping in touch with loved ones by phone or online, and by exercising at home.")
    else : 
        action = "" 
        



    subject = "COVID-19 Diagnosis - " + dt_string
    body = (greeting + " your COVID-19 diagnosis performed at " + 
            dt_string + " at " + currentTime + " has returned the following results:\n\n " + 
            resultText + "\n\n" + action)
    sender_email = "utechmohexpertsystem2021@gmail.com"
    receiver_email = email
    password = "Password@15"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

def send_alert(totVhr,totHr,totLr,totNr):
        # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%B %d, %Y")
    currentTime = datetime.now()
    if currentTime.hour < 12 :
        greeting = ('Good morning,')
    elif 12 <= currentTime.hour < 18 :
        greeting = ('Good afternoon,')
    else :
        greeting = ('Good evening,')
    
    currentTime = str(time.strftime('%I:%M %p'))
    subject = "Spike in COVID-19 High Risk Diagnoses - " + dt_string
    body = (greeting + " please note that there has been an unusual spike in high risk diagnosis results. \n "
             "As of " + dt_string + " at " + currentTime + ", there has been " + str(totVhr) + " very high risk results,  "
             + str(totHr) + " high risk results, " + str(totLr) + " low risk results and " 
             + str(totNr) + " results reported at no risk. Please see the attached spreadsheet for diagnoses to date.")

    sender_email = "utechmohexpertsystem2021@gmail.com"
    receiver_email = "utechmohexpertsystem2021@gmail.com"
    password = "Password@15"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "data/diagnoses.xlsx"  # In same directory as script
    filenameWithoutDir =os.path.basename(filename)

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filenameWithoutDir}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)