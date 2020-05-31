import smtplib
import getpass
from email.mime.text import MIMEText
from I_O import *
import tkinter as tk
from tkinter import simpledialog

def e_mail():
    a = open("config.txt", "r")
    line = a.read()
    cred=line.split(":")
    email = cred[0]
    passwd = cred[1]
    speak("Enter your target email: ")
    root = tk.Tk()
    root.withdraw()
    inp = simpledialog.askstring(title="User Input", prompt="Enter target email: ")
    target = inp
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