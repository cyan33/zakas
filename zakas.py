# Please first install all the dependencies from README

import speech_recognition as sr
import os
from time import ctime
from getch import getch
from gtts import gTTS


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def zakas(data):
    if "how are you" in data:
        speak("I am fine")

    if ("marriage" in data or "sex" in data) and ("you" in data or "your" in data):
        speak("I don't feel like talking about my personal life")

    if "time" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Chang, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


# initialization
speak("Hi Chang, How can I help you?")
while 1:
    print("press Enter to say something to Zakas!")
    if getch() == "\n":
        data = recordAudio()
        zakas(data)
