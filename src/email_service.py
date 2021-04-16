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
    body = (greeting + " your COVID-19 diagnosis performed at " + 
            dt_string + " at " + currentTime + " has returned the following results:\n\n " + 
            resultText)
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