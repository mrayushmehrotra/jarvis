import pyttsx3
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text
import os
import subprocess as sp
import pyautogui
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

def open_camera():
    try:
        sp.run('xdg-open camera:', shell=True)
    except Exception as e:
        print(f"Error: {e}")

open_camera()
def open_terminal():
    try:
        sp.Popen(['gnome-terminal'])  
    except Exception as e:
        print(f"Error: {e}")
open_terminal()

USERNAME = config("USER")
BOTNAME = config("BOTNAME")

# espeak for Linux
engine = pyttsx3.init('espeak')

# speech rate
engine.setProperty("rate", 190)

# volume
engine.setProperty("volume", 1.0)
# set Voices
voices = engine.getProperty("voices")

engine.setProperty("voice", 'inc')

def speak(text):
    engine.say(text)
    engine.runAndWait()

# GREET USER FN
def greet_user():
    speak(opening_text)
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
            

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-in")
        if "exit" in query or "stop" in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good Night Sir, take care")
            else:
                speak("Have a Good Day")
            exit()
    except Exception as e:
        speak("Sorry, I could not understand. Could you please say that again?")
        query = "None"
        print(e)
        return query

# LAST FUNCTION WHICH WILL CALL ALL THE FUNCTIONS
greet_user()
take_user_input()
