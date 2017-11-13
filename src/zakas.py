from getch import getch
from time import ctime

from handlers.Youtube import Youtube
from handlers.Google import Google
from dict import dict
from utils import *


class Zakas:
    def __init__(self):
        pass

    def respond(self, data):
        # loop through the basic / hard-coded responses
        for keyword, res in dict.items():
            if keyword in data:
                speak(res)
                return

        # todo: move these to a separated handler utility file
        if "time" in data:
            speak(ctime())
            return

        if "where is" in data:
            data = data.split(" ")
            location = data[2]
            speak("Hold on, I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
            return

        if "youtube" in data:
            y = Youtube(data)
            y.play()
            return

        if "google" in data:
            g = Google(data)
            g.search()
            return

        # if voice msg not comprehended
        speak("I'm truly sorry. Didn't get what you meant.")

        return


if __name__ == '__main__':
    z = Zakas()
    greeting()

    while True:
        println("press Enter to say something to Zakas, or '0' to exit")
        user_input = getch()
        if user_input == "\n":
            z.respond(record())
        elif user_input == "0":
            goodbye()
            break

