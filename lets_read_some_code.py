import urllib.request as urllib

from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site= site

    def scrape(self):
        response = urllib.urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        for tag in soup.find_all('a'):
            url = tag.get('href')
            if url and 'html' in url:
                print('\n'+url)


Scraper('http://news.google.com/').scrape()