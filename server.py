import flask

import wuxia

app = flask.Flask(__name__)


@app.route('/wuxia')
def wuxia_feed():
    if 'c' in flask.request.args:
        categories = flask.request.args['c'].split(',')
    else:
        categories = None
    soup = wuxia.filter_by_categories(categories)
    resp = flask.make_response(soup.prettify(), 200)
    resp.headers['Content-Type'] = 'application/rss+xml'
    return resp


if __name__ == '__main__':
    app.debug = True
    app.run()
