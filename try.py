import pyttsx3
import wikipedia

engine = pyttsx3.init() #initialise
a = engine.say("Football")
engine.say(wikipedia.search("Football"))
engine.runAndWait()