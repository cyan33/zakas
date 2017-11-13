import sys
import webbrowser
sys.path.append('../')
from utils import *

from voice_processing import filter_google

class Google:
    def __init__(self, voice):
        speak("Hold on, I'm searching the result on Google.")
        self.term = filter_google(voice)
        return

    def build_query(self):
        return 'https://www.google.com/search?q=' + self.term

    def search(self):
        webbrowser.open(self.build_query())

if __name__ == '__main__':
    g = Google('search alexa from google')
    g.search()
