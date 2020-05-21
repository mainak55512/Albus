"""

    Program Name: Albus.py,  Description: Voice Assistant
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
'''
##############################################################################

This ia an AI virtual assistant named A.L.B.U.S.
A.L.B.U.S. stands for "Artificial Logistic Backend UNIX-based Subordinate".
It can do several *nix based operations without any user interaction, 
the only thing needed is the voice command from the user.

##############################################################################
'''

import speech_recognition as sr
import os
import datetime
import threading
import wikipedia
import webbrowser

wb = webbrowser.get('epiphany') # firefox or chrome can also be used if the machine has enough resources, in that case 'epiphany' should be replaced by 'firefox' or 'google-chrome' accordingly.

def event_loop():
    import pyglet
    animation = pyglet.image.load_animation('2RNb.gif')
    anim = pyglet.sprite.Sprite(animation)
    w = anim.width
    h = anim.height

    win = pyglet.window.Window(width=w, height=h)
    win.set_caption('A.L.B.U.S.')

    r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
    pyglet.gl.glClearColor(r, g, b, alpha)

    @win.event
    def on_draw():
        win.clear()
        anim.draw()
    pyglet.app.run()

def speak(audio):
    '''This will speak the text'''

    os.system(f"flite -voice ./cmu_us_rms.flitevox -t '{audio}'")  # flite module needs to be installed. I haven't use the pyttsx3 module instead used the actual tts engine and ran it in a subshell to get the voice output. os.system() allows us to run shell commands from inside the python interpreter.


def greet():
    '''this function greets the master'''

    hr = int(datetime.datetime.now().hour)# hr holds the integer value of hour
    if hr >= 0 and hr < 12:
        speak("good morning sir")
    elif hr >= 12 and hr < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("I am,  Albus, your personal assistant. How can I help you?")


def command():
    '''This function takes the voice command from the master'''

    cmd = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n\nListning...")
        cmd.pause_threshold = 1 # this makes the interpreter to hold for a second
        audio = cmd.listen(source)  # takes the master's voice commands
        
        try:                   # this ma give error, so try/except is used here.
            print("Recognizing...")
            query = cmd.recognize_google(audio, language='en-in')
            print(f"Received_command: {query}\n")
        except Exception as e:
            speak("I can't get that...")
            return "Sorry!"
        return query # returns the query to the other methods who will call the command() method
if __name__ == "__main__":  # this is the main method of this python program

    print("Albus.py  Copyright (C) 2020  Mainak Bhattacharjee\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions.\n\n")
    # t1 = threading.Thread(target=event_loop)
    # t1.start()
    greet()
    
    while True:
        query = command().lower()
        if 'who are you' in query:
            speak("I am Albus, Albus stands for Artificial, logistic, Backend, Unix-based Subordinate")
        elif 'wikipedia' in query:
            try:
                speak("searching in wikipedia...")
                query = query.replace("wikipedia", "")  #replaces 'wikipedia' keyword with blank
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(f"According to wikipedia {result}")
            except Exception as e:
                speak("Sorry sir, no results found")
        elif 'open youtube' in query:
            speak("opening youtube")
            wb.open('https://www.youtube.com')
        elif 'open google' in query:
            speak("opening google")
            wb.open("https://google.com")
        elif 'open github' in query:
            speak("opening github")
            wb.open("https://github.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            wb.open("web.whatsapp.com")