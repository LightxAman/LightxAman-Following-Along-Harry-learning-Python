# PS 1.3: Write a Python program that uses the pyttsx3 module to say “Hey I am good”


import pyttsx3

engine = pyttsx3.init()
engine.say("Hey I am good")
engine.runAndWait()
