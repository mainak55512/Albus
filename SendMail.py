"""

    Program Name: SendMail.py,  Description: part of the Voice Assistant
    Copyright (C) 2020  Mainak Bhattacharjee

    Albus.py is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Albus.py is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    e-mail: mbhattacharjee432@gmail.com

"""

import smtplib
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