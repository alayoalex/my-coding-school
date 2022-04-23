import requests


def downloading():
    url = 'http://www.arxiv-sanity.com/'
    html = requests.get(url)

    with open('resources/arvixindex.txt', 'wb') as r: 
        r.write(html.content)

downloading()

