import pyttsx3 as p
import speech_recognition as sr
import datetime

from selenium_web import inflow
from youtube_automation import * 
from weather import *
from news import *
from jokes import *
import randfacts
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='./Authentication.json'
# D:/voice asst-python/asst.json

engine = p.init()

# *********Rate**********
rate = engine.getProperty('rate')
# print(rate)
engine.setProperty('rate', 140)
print(rate)

# *********Voices*********
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices)

# engine.say("Heya, You can do it.")
# engine.runAndWait()


def speak(text):
    engine.say(text)
    engine.runAndWait()


today_date=datetime.datetime.now()


r = sr.Recognizer()

speak("Heya, I'm your voice assistant. Temperature im Ranchi is" + str(temp())+ "and with" + str(des()))
speak("Today is " + today_date.strftime("%d") + " " + today_date.strftime("%B") + "and it's currently" + today_date.strftime("%w"))


with sr.Microphone() as source:

    r.energy_threshold = 1000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I am very well")
speak("What can I do for you?")

with sr.Microphone() as source:

    r.energy_threshold = 1000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening..")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("Information of which topic do you want?")
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    assist = inflow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("What type of video do you want?")
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        video = r.recognize_google(audio)
    speak("searching {} in youtube".format(video))
    assist = music()
    assist.play(video)


elif "news" in text2:
    speak("Sure, These are some news headlines")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" and "facts" in text2:
    x=randfacts.getFact()
    print(x)
    speak("Did you know that"+ x)

elif "joke" or "jokes" in text2:
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])