# Please first install all the dependencies from README
import os
import speech_recognition as sr
from getch import getch
from gtts import gTTS
from time import ctime

from handlers.Youtube import Youtube
from dict import dict
from utils import println


class Zakas:
    def __init__(self):
       pass

    def speak(self, audioString):
        println(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

    def recordAudio(self):
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("How can I help you?")
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio)
            println("You said: " + data)
        except sr.UnknownValueError:
            println("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            println("Could not request results from Google Speech Recognition service; {0}".format(e))

        return data.lower()


    def respond(self, data):
        # loop through the basic responses
        for keyword, res in dict.items():
            if keyword in data:
                self.speak(res)
                return

        # todo: move these to a separated handler utility file
        if "time" in data:
            self.speak(ctime())
            return

        if "where is" in data:
            data = data.split(" ")
            location = data[2]
            self.speak("Hold on Chang, I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
            return

        if "youtube" in data:
            self.speak("Hold on, I'm searching the result on Youtube.")
            y = Youtube(data)
            y.play()
            return


        # if voice msg not comprehended
        self.speak("I'm truly sorry. My dictionary is rather poor right now and cannot get what you meant. Do you have any interest in contributing my dictionary,in the following url?")
        println("https://github.com/thomasyimgit/zakas")
        return


if __name__ == '__main__':
    z = Zakas()
    # z.speak("Lord cast your light upon us. For the night is dark and full of terrors.")

    while True:
        println("press Enter to say something to Zakas, or '0' to exit")
        user_input = getch()
        if user_input == "\n":
            z.respond(z.recordAudio())
        elif user_input == "0":
            break

