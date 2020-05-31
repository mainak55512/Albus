"""

    Program Name: I_O.py,  Description: part of the Voice Assistant
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

import speech_recognition as sr
import os

def speak(audio):
    '''This will speak the text'''

    os.system(f"flite -voice ./cmu_us_rms.flitevox -t '{audio}'")  # flite module needs to be installed. I haven't use the pyttsx3 module instead used the actual tts engine and ran it in a subshell to get the voice output. os.system() allows us to run shell commands from inside the python interpreter.


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