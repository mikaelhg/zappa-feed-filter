import bs4
import requests

__FEED_URL = 'http://www.wuxiaworld.com/feed/'


def filter_by_categories(categories):
    input_feed = requests.get(__FEED_URL)
    soup = bs4.BeautifulSoup(input_feed.text, 'xml')

    for i in soup.find_all('item'):
        found = False
        for c in i.find_all('category'):
            if categories and c.string in categories:
                found = True

        if not found:
            i.extract()

    return soup
