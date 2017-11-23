from getch import getch

from handlers.Youtube import Youtube
from handlers.Google import Google
from chat import Bot
from utils import *


class Zakas:
    def __init__(self):
        self.bot = Bot()
        pass

    def respond(self, data):
        # todo: move these to a separated handler utility file

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

        self.bot.respondTo(data)
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

