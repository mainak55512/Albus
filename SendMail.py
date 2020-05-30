import smtplib
import getpass
from email.mime.text import MIMEText
from I_O import *

def e_mail():
    a = open("config.txt", "r")
    line = a.read()
    cred=line.split(":")
    email = cred[0]
    passwd = cred[1]
    speak("Enter your target email: ")
    target = input("Enter your target email: ")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, passwd)
    speak("Enter your mail subject ")
    Subject = command()
    speak("Enter the email body")
    body = command()
    message = MIMEText(body)
    message["Subject"] = Subject
    message["From"] = email
    message["To"] = target
    server.sendmail(email, target, message.as_string())
    speak("Email sent successfully")