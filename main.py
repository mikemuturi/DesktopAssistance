import pyttsx3 as p
import speech_recognition as sr
import randfacts
import pywhatkit
from pywhatkit.remotekit import start_server
from flask import Flask, request
import datetime

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)
def speak(text):
    engine.say(text)
    engine.runAndWait()
# engine.say('Hello mike, my name is picky your virtual desktop assistance, what can i do for you?')
# engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>8 and hour<12:
        return ("morning")
    elif hour>=12 and hour<16:
        return ("afternoon")
    else:
        return ("evening")


today_date=datetime.datetime.now()
r = sr.Recognizer()

speak('Hello mike, my name is picky your virtual desktop assistance,how are you?')

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak('i am fine too mike')
    speak('what can i do for you')

# if "fact" or "facts" in text:
#     speak("sure ,")
#     x=randfacts.getFact()
#     print(x)
#     speak("Did you know that,"+x)

elif "time" or "date" in text:
    speak("today is"+today_date.strftime("%d")+"of"+today_date.strftime("%B")+"and its currently"+
          (today_date.strftime("%I"))+(today_date.strftime("%M"))+(today_date.strftime("%p")))
if 'play ' and "youtube" in text:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    song = speak(text)
    speak("playing"+song)
    pywhatkit.playonyt(song)