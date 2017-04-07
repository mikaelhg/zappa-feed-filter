import bs4
import re

__RE_WHITE_SPACE_LINE = re.compile('^[\s]$')

__OK_ATTRS = {
    'a': ['href'],
    'img': ['src']
}


def clean_attrs(tag):
    """
    :type tag: bs4.element.Tag
    :rtype: None
    """
    for k, v in list(tag.attrs.items()):
        if k.startswith('data-') or k in ('style', 'class', 'srcset'):
            del tag.attrs[k]


def clean_tags(soup):
    """
    :type soup: bs4.BeautifulSoup
    :rtype: None
    """
    for tag in soup.find_all(True):
        if tag.name in ('span', 'div', 'p', 'a', 'br', 'hr', 'strong', 'b', 'i', 'h1', 'h2', 'h3'):
            clean_attrs(tag)
        else:
            tag.extract()

    for element in soup(text=lambda text: isinstance(text, bs4.Comment)):
        element.extract()

    for p in soup.find_all('p', text=__RE_WHITE_SPACE_LINE):
        p.extract()
