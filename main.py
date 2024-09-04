import pyttsx3 as p
import speech_recognition as sr

from selenium_web import inflow
from youtube_automation import * 
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


r = sr.Recognizer()

speak("Heya, I'm your voice assistant")

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
