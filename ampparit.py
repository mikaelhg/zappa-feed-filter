import bs4
import requests

__FEED_URL = 'http://feeds.feedburner.com/ampparit-it'

__SHITTY_SOURCES = [
    'Iltalehti',
    'Mobiili.fi',
    'Mikrobitti.fi',
    'MTV.fi',
    'Suomimobiili',
    'Ilta-Sanomat',
    'Suomen Kuvalehti'
]


def filter_shitty_sources():
    input_feed = requests.get(__FEED_URL)
    soup = bs4.BeautifulSoup(input_feed.text, 'xml')

    for i in soup.find_all('entry'):
        try:
            author = i.find('author').find('name').string
            if author in __SHITTY_SOURCES:
                i.extract()
        except:
            pass

    return soup
