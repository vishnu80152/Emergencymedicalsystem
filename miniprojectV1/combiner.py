from time import clock_settime
import pyttsx3
import datetime
import speech_recognition as sr
import os
import cv2
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#txt to spch
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>= 0 and hour<=12:
        speak('good morning')
    elif hour>12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening') 
    
    speak('Hi iam EMS System here to warn you that your condition for driving is not good Please take a break or, a nap')
