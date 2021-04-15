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
    dt_string = now.strftime("%d/%m/%Y")

    currentTime = int(time.strftime('%H'))   
    if currentTime < 12 :
        greeting = ('Good morning,')
    if currentTime > 12 :
        greeting = ('Good afternoon,')
    if currentTime > 6 :
        greeting = ('Good evening,')
    
    currentTime = str(time.strftime('%I:%M %p'))
    subject = "COVID-19 Diagnoses - " + dt_string
    body = greeting + "please see attached for a spreadsheet containing diagnoses as of " + dt_string + " at " + currentTime + "."
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

