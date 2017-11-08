from bs4 import BeautifulSoup
import urllib2
import webbrowser

from src.handlers.voice_processing import filter_youtube
from src.utils import println

class Youtube:
    def __init__(self, voice):
        self.url = self.buildQuery(voice)

    def buildQuery(self, voice):
        # data is the voice string passed by zakas
        voice = filter_youtube(voice)

        url = 'https://www.youtube.com/results?search_query=' + '+'.join(voice.split(' '))
        println(url)
        return url

    def getVideoUrl(self):
        # analyze html content and get redirection url
        content = urllib2.urlopen(self.url).read()
        soup = BeautifulSoup(content, "html.parser")

        song = soup.select_one('#results div[class="yt-lockup-content"]')

        if not song:
            return False

        # filter out the ads and banners
        while True:
            # if can find span[class="yt-badge-ad"], then it's an ad
            span_list = song.select('span')
            for span in span_list:
                if 'yt-badge-ad' in span['class']:
                    song = song.find_next('div', {'class': 'yt-lockup-content'})
            else:
                break

        # song_title = song.find('a', {'class': "spf-link"})['title']
        # speak('Playing ' + song_title)
        return 'https://www.youtube.com' + song.find('a', {'class': "spf-link"})['href']

    def play(self):
        webbrowser.open(self.getVideoUrl())
        return

if __name__ == '__main__':
    # test
    y = Youtube('Play shape of you from youtube')
    y.play()
