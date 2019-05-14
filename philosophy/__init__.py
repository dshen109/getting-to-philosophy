from contextlib import closing
from urllib.request import urlopen

import bs4


def get_page_title(soup):
    """
    Get the page title from the top-level html.
    """
    return soup.title.contents[0].replace(' - Wikipedia', '')


def get_first_link(soup):
    """
    Get the first link from a page.
    """
    paragraphs = soup.find('div', {"class": "mw-parser-output"}).find_all('p')

    for p in paragraphs:
        links = p.find_all('a')
        if not links:
            continue
        for l in links:
            if ispagelink(l):
                return getlink(l)

    raise RuntimeError("Couldn't find a hyperlink.")


def ispagelink(tag):
    return True


def getlink(tag):
    """
    Get the hyperlink and title from a tag.

    Return None tuple if there isn't a link.
    """
    if not tag or isinstance(tag, str):
        return None, None
    if "href" not in tag.attrs:
        return None, None
    return tag["href"], tag["title"]


if __name__ == "__main__":
    page = 'https://en.wikipedia.org/wiki/Randomness'

    text = None

    with closing(urlopen(page)) as p:
        text = p.read()

    soup = bs4.BeautifulSoup(text, features='html.parser')
    # print(soup.body.div)
    paragraphs = soup.find('div', {"class": "mw-parser-output"}).find_all('p')
    # print(paragraphs[0].__dict__.keys())
    # print(paragraphs[0].contents)
    # print(paragraphs[1].contents)
    print(get_page_title(soup))
    print(get_first_link(soup))
