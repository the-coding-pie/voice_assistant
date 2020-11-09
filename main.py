# all our imports
import speech_recognition as sr
from time import sleep
from datetime import datetime
import webbrowser
import pyttsx3


# make an instance of Recognizer class
r = sr.Recognizer()


# confs for pyttsx3
engine = pyttsx3.init()
""" RATE """
engine.setProperty('rate', 125)
""" VOLUME """
engine.setProperty('volume', 0.8)


""" speak (text to speech) """
def speak(text):
  engine.say(text)
  engine.runAndWait()


""" fn to recognize our voice and return the text_version of it"""
def recognize_voice():
  text = ''

  # create an instance of the Microphone class
  with sr.Microphone() as source:
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)

    # capture the voice
    voice = r.listen(source)

    # let's recognize it
    try:
      text = r.recognize_google(voice)
    except sr.RequestError:
      speak("Sorry, the I can't access the Google API...")
    except sr.UnknownValueError:
      speak("Sorry, Unable to recognize your speech...")
  return text.lower()


""" fn to respond back """
def reply(text_version):
  # name
  if "name" in text_version:
    speak("My name is JARVIS")
  
  # how are you?
  if "how are you" in text_version:
    speak("I am fine...")

  # date
  if "date" in text_version:
    # get today's date and format it - 9 November 2020
    date = datetime.now().strftime("%-d %B %Y")
    speak(date)

  # time
  if "time" in text_version:
    # get current time and format it like - 02 28 
    time = datetime.now().time().strftime("%H %M")
    speak("The time is " + time)
  
  # search google
  if "search" in text_version:
    speak("What do you want me to search for?")
    keyword = recognize_voice()

    # if "keyword" is not empty
    if keyword != '':
      url = "https://google.com/search?q=" + keyword

      # webbrowser module to work with the webbrowser
      speak("Here are the search results for " + keyword)
      webbrowser.open(url)
      sleep(3)
  
  # quit/exit
  if "quit" in text_version or "exit" in text_version:
    speak("Ok, I am going to take a nap...")
    exit()


# wait a second for adjust_for_ambient_noise() to do its thing
sleep(1)

while True:
  speak("Start speaking...")
  # listen for voice and convert it into text format
  text_version = recognize_voice()

  # give "text_version" to reply() fn
  reply(text_version)