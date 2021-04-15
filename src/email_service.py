import smtplib, ssl

port = 465  # For SSL
password = "Password@15"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("utechmohexpertsystem2021@gmail.com", password)
    sender_email = "utechmohexpertsystem2021@gmail.com"
    receiver_email = "utechmohexpertsystem2021@gmail.com"
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)
