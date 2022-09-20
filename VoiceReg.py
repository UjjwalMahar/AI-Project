from distutils.cmd import Command
from gettext import find
import speech_recognition as sr
import pyaudio
import wikipedia as wk
import pyttsx3
import webbrowser as wb
    
engine = pyttsx3.init() #initialise

listener = sr.Recognizer()

try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            if (command == "open Google"):
                url = "www.google.com"
                wb.open(url)
            if (command == "open Wikipedia"):
                engine.say("What do you want to search  ? ")
                print("What do you want to search  ? ")
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                print(command)
                # print(type(command))
                engine.say(wk.search(command))
                print(wk.search(command))
                engine.runAndWait()

except:
        print("Something else went wrong")
        pass    

