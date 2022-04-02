import json

import pyttsx3 as p
import requests
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
import ctypes
import winshell
import pyjokes
import subprocess
import smtplib

import randfacts
# import pywhatkit
# from pywhatkit.remotekit import start_server
# from flask import Flask, request


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)
def talk(audio):
    engine.say(audio)
    engine.runAndWait()
# engine.say('Hello there,Im your Intelligent  desktop voice assistance, what can i do for you?')
engine.runAndWait()

def rec_audio():
    recog =sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening..')
        audio = recog.listen(source)

        data=''

        try:
            data=recog.recognize_google(audio)
            print('you said: '+ data)



        except sr.UnknownValueError:
            print('Assistant could not understand the audio')

        except sr.RequestError as ex:
            print('Request Error from google speech recognition' + ex)

        return data

rec_audio()

def response(text):
    print(text)

    tts=gTTS(text=text,lang='en')

    audio ="Audio.mp3"
    tts.save(audio)


    playsound.playsound(audio)

    os.remove(audio)

def call(text):
    action_call='assistant'

    text=text.lower()

    if action_call in text:
        return True

    return False

def today_date():
    now =datetime.datetime.now()
    date_now=datetime.datetime.today()
    week_now=calendar.day_name[date_now.weekday()]
    month_now=now.month
    day_now=now.day

    months=  [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]

    ordinals =[
        '1st',
        '2nd',
        '3rd',
        '4th',
        '5th',
        '6th',
        '7th',
        '8th',
        '9th',
        '10th',
        '11th',
        '12th',
        '13th',
        '14th',
        '15th',
        '16th',
        '17th',
        '18th',
        '19th',
        '20th',
        '21st',
        '22nd',
        '23rd',
        '24th',
        '25th',
        '26th',
        '27th',
        '28th',
        '29th',
        '30th',
        '31st',

    ]

    return f'Today is{week_now},{months[month_now-1]} the {ordinals[day_now-1]}.'

def say_hello(text):
    greetings = ['hi','hello','hey there','morning','afternoon','evening']

    response = ['hi','hello','hey there','morning','afternoon','evening']

    for word in text.split():
        if word.lower() in greetings:
            return random.choice(response) +  "."
    return  " "

def wiki_person(text):
    list_wiki =text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <=len(list_wiki)-1 and list_wiki[i].lower() == 'who' and list_wiki[i+1].lower() == 'is':
            return list_wiki[i+2] +' '+ list_wiki[i + 3]

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-")+"-note.txt"
    with open(file_name,"w")as f:
        f.write(text)

    subprocess.Popen(["notepad.exe",file_name])

def send_email(to,content):
    server = smtplib.SMTP("smtp.gmail.com")
    server.ehlo()
    server.starttls()

    server.login("mikemuturi657@gmail.com", "Mike_1999")
    server.sendmail("email", to, content)
    server.close()


while True:

    try:
        text = rec_audio()
        speak = " "

        if call(text):

            speak = speak + say_hello(text)

            if 'date' in text or 'day' in text or 'month' in text:
                get_today = today_date()
                speak = speak +" " + get_today

            elif 'time' in text:
                now = datetime.datetime.now()
                meridean= ""
                if now.hour >= 12:
                    meridean = 'p.m'
                    hour = now.hour - 12
                else:
                    meridean= 'a.m'
                    hour = now.hour
                if now.minute < 10:
                    minute = '0'+str(now.minute)

                else:
                    minute=str(now.minute)
                speak= speak + " " + 'it is' + str(hour) +":" +minute+ " " +meridean+ " ."

            elif 'wikipedia' in text or 'wikipedia' in text:
                if 'who is ' in text:
                    person= wiki_person(text)
                    wiki= wikipedia.summary(person,sentenses=2)
                    speak= speak+" "+ wiki
            elif 'who are you ' in text:
                speak = speak + """" i'm your intelligent desktop assistance"""

            elif 'your name' in text:
                speak = speak + "my name is your assistant"

            elif 'who am i' in text:
                speak = speak + 'probably a human being'
            elif "how are you " in text:
                speak =speak + "I am fine, Thank you"
                speak = speak +"\nHow are you"

            elif 'fine 'in text or 'good' in text:
                speak= speak + "it is good to know you are fine"

            elif 'open' in text.lower():
                if 'chrome' in text.lower():
                    speak= speak+ 'opening google chrome'
                    os.startfile(r"C:\Program Files\Google\Chrome \Application\chrome.exe")

                elif 'word' in text.lower():

                    speak= speak+ 'opening microsoft word '
                    os.startfile(r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE")

                elif 'android' in text.lower():
                    speak = speak + 'opening android studio'
                    os.startfile(r"C:\Program Files\Android\Android Studio\bin\studio64.exe")

                elif 'Visual Studio' in text.lower():
                    speak = speak + 'opening vs code'
                    os.startfile(r"C:\Users\Mike\AppData\Local\Programs\Microsoft VS Code\Code.exe")

                elif 'sublime text' in text.lower():
                    speak = speak + 'opening sublime text'
                    os.startfile(r"C:\Program Files\Sublime Text 3\sublime_text.exe")

                elif 'Boom Play' in text.lower():
                    speak = speak + 'opening Groove Music'
                    os.startfile(r"C:\Users\Mike\Music\Playlists\boom play.zpl")

                elif 'youtube' in text.lower():
                    speak = speak + 'opening Youtube'
                    webbrowser.open("https://youtube.com/")
                elif 'google' in text.lower():
                    speak = speak + 'opening Google'
                    webbrowser.open('https://google.com')
                elif 'stack overflow' in text.lower():
                    speak = speak + "opening StackOverFlow"
                    webbrowser.open("https://stackoverflow/")
                elif 'laikipia university' in text.lower():
                    speak = speak + "opening LaikipiaUniversity website"
                    webbrowser.open("https://laikipia.ac.ke/")

                else:
                    speak = speak +"Application not available"

            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "http://www.youtube.com/result?search_query=" +
                    "+".join(search)
                )
                speak = speak + "opening" + str(search) + "on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search)
                )
                speak = speak + "searching"+ str(search) + "on google"

            elif "google" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open("https://www.google.com/search?q="+ "+".join(search))
                speak = speak + "search" + str(search)+ "on google"
            elif "change wallpaper" in text or "change background" in text:
                img = r'C:\Users\Mike\Desktop\wallpaper'
                list_img = os.listdir(img)
                imageChoice = random.choice(list_img)
                randomImg= os.path.join(img,imageChoice)
                ctypes.windll.user32.systemparametersInfow(20, 0, randomImg, 0)
                speak = speak + "Background dispaly changed successfully"

            elif 'play music' in text or 'playsong' in text:
                talk('playing')
                music_dir = r'C:\Users\Mike\Desktop\playmusic'
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                random = os.path.join(music_dir, d)
                playsound.playsound(random)

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True,show_progress=False, sound=True
                )
                speak = speak + "Recycle bin Emptied Successfully"

            elif "note" in text or "write this" in text or "take note" in text or "pen down" in text:
                talk("What should i write")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "i have made note on that"

            elif "jokes" in text or "tell a joke" in text:
                speak = speak + pyjokes.get_joke()


            elif "where is" in text or "locate" in text or "location of" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind +  1:]
                url = "https://www.google.com/maps/place"+"".join(location)
                speak = speak + "This is where"+ str(location)+ "is."
                webbrowser.open(url)

            elif "email to computer" in text or "gmail to computer" in text:
                try:
                    talk("what should i email")
                    content = rec_audio()
                    to = "Reciever email address"
                    send_email(to,content)
                    speak = speak + "Email has been sent!"
                except Exception as e:
                    print(e)
                    talk("Error 101 occurred, try again")

            elif "email" in text or "gmail" in text:
                try:
                    talk("Email message to be sent")
                    content = rec_audio()
                    talk("who is receiver")
                    to = input("Enter address")
                    send_email(to, content)
                    speak = speak + "Email has been sent"
                except Exception as e:
                    print(e)
                    speak = speak + "Email not sent an error occurred try again"
            elif "news" in text or "updates" in text:
                url = ('https://newsapi.org/v2/everything?' 
                       'q=Apple&'
                       'from=2022-03-11&'
                       'sortBy=popularity&'
                       'apiKey=7437bfd225fa44fca4e1dbf61aff4fea')

                try:
                    response = requests.get(url)

                except:
                    talk("please check your connection")

                news = json.loads(response.text)

                for new in news["articles"]:
                    print(str(new["title"])),"\n"
                    talk(str(new["title"]))
                    engine.runAndWait()

                    print(str(new["description"]),"\n")
                    talk(str(new["description"]))
                    engine.runAndWait()




















            




            response(speak)

    except:
        talk('')











#
# def wishme():
#     hour=int(datetime.datetime.now().hour)
#     if hour>8 and hour<12:
#         return ("morning")
#     elif hour>=12 and hour<16:
#         return ("afternoon")
#     else:
#         return ("evening")
#
#
# today_date=datetime.datetime.now()
# r = sr.Recognizer()
#
# speak('Hello mike, my name is picky your virtual desktop assistance,how are you?')
#
# with sr.Microphone() as source:
#     r.energy_threshold=10000
#     r.adjust_for_ambient_noise(source,1.2)
#     print("listening...")
#     audio = r.listen(source)
#     text = r.recognize_google(audio)
#     print(text)
#
# if "what" and "about" and "you" in text:
#     speak('i am fine too mike')
#     speak('what can i do for you')
#
# # if "fact" or "facts" in text:
# #     speak("sure ,")
# #     x=randfacts.getFact()
# #     print(x)
# #     speak("Did you know that,"+x)
#
# elif "time" or "date" in text:
#     speak("today is"+today_date.strftime("%d")+"of"+today_date.strftime("%B")+"and its currently"+
#           (today_date.strftime("%I"))+(today_date.strftime("%M"))+(today_date.strftime("%p")))
# if 'play ' and "youtube" in text:
#     r.energy_threshold = 10000
#     r.adjust_for_ambient_noise(source,1.2)
#     print("listening...")
#     audio = r.listen(source)
#     text = r.recognize_google(audio)
#     song = speak(text)
#     speak("playing"+song)
#     pywhatkit.playonyt(song)