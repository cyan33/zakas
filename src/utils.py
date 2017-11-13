from __future__ import print_function
import os
import speech_recognition as sr
from colorprint import *
from gtts import gTTS


def println(words):
    print(words, color="yellow")

def warn(words):
    print(words, color="red")

def speak(audio_string):
    println(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def record():
    # record audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("How can I help you?")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        println("You said: " + data)
    except sr.UnknownValueError:
        warn("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        warn("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data.lower()
