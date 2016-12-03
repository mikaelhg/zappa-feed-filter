import bs4

import requests
from flask import Flask, make_response


app = Flask(__name__)


@app.route('/wuxia')
def wuxia():
    input_feed = requests.get('http://www.wuxiaworld.com/feed/')
    soup = bs4.BeautifulSoup(input_feed.text, 'xml')

    for i in soup.find_all('item'):
        found = False
        for c in i.find_all('category'):
            if c.string == 'Desolate Era':
                found = True

        if not found:
            i.extract()

    resp = make_response(soup.prettify(), 200)
    resp.headers['Content-Type'] = 'application/rss+xml'
    return resp


if __name__ == '__main__':
    app.debug = True
    app.run()
