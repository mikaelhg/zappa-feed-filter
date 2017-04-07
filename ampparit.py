import bs4
import requests
from urlparse import urlparse
from fake_useragent import UserAgent

__FEED_URL = 'http://feeds.feedburner.com/ampparit-it'

__SHITTY_SOURCES = [
    'Iltalehti',          # the two worst quality daily papers in Finland
    'Ilta-Sanomat',
    'MTV.fi',             # "entertainment"
    'Mikrobitti.fi',      # ads disguised as "leaks" of new mobile phone models
    'Puhelinvertailu.com',
    'Mobiili.fi',
    'SuomiMobiili',
    'Suomen Kuvalehti'    # useless chaff
]

__SHITTY_DOMAINS = [
    'www.iltasanomat.fi',
    'www.is.fi'
]

__headers = {'User-Agent': UserAgent().chrome}


def filter_shitty_sources():
    """
    :rtype: bs4.BeautifulSoup
    """
    input_feed = requests.get(__FEED_URL)
    soup = bs4.BeautifulSoup(input_feed.text, 'xml')

    for i in soup.find_all('entry'):
        try:
            author = i.find('author').find('name').string
            if author in __SHITTY_SOURCES:
                i.extract()
        except AttributeError:
            pass

    soup.feed.title.string = 'Ampparit.com IT filtered'

    self_link = soup.find('link', {'rel': 'self'})
    if self_link:
        self_link['href'] = 'https://mikael.io/api/rss/ampparit'

    for tag in soup.find_all('link', {'rel': 'alternate'}):
        link = get_actual_link(tag.attrs['href'])
        url = urlparse(link)
        if url.netloc in __SHITTY_DOMAINS:
            tag.parent.extract()
        else:
            tag.attrs['href'] = link
            tag.parent.id.string = link

    return soup


def get_actual_link(url):
    """
    :type url: str
    :rtype: str
    """
    response = requests.head(url, timeout=1)
    if response and 'Location' in response.headers:
        return response.headers['Location']
    else:
        return url


def get_content(url):
    page = requests.get(url, headers=__headers)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')


