import bs4
import requests

__FEED_URL = 'http://feeds.feedburner.com/ampparit-it'

__SHITTY_SOURCES = [
    'Iltalehti',          # the two worst quality daily papers in Finland
    'Ilta-Sanomat',
    'MTV.fi',             # "entertainment"
    'Mikrobitti.fi',      # ads disguised as "leaks" of new mobile phone models
    'Puhelinvertailu.com',
    'Mobiili.fi',
    'Suomimobiili',
    'Suomen Kuvalehti'    # useless chaff
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
