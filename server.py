import flask

import wuxia, ampparit

app = flask.Flask(__name__)


@app.route('/api/rss/wuxia')
def wuxia_feed():
    if 'c' in flask.request.args:
        categories = flask.request.args['c'].split(',')
    else:
        categories = None
    feed = wuxia.filter_by_categories(categories)
    return feed.prettify(), 200, {'Content-Type': 'application/rss+xml; charset=utf-8'}


@app.route('/api/rss/ampparit')
def ampparit_feed():
    feed = ampparit.filter_shitty_sources()
    return feed.prettify(), 200, {'Content-Type': 'application/atom+xml; charset=utf-8'}


if __name__ == '__main__':
    from os import getuid
    app.debug = (getuid() == 1000)
    app.run()
