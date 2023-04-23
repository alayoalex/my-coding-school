import os
import urllib.request
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

PROXY_HOST = "localhost:5555"
PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
DOWNLOAD_PATH = os.path.join(PROJECT_DIR, 'DESCARGAS')

def get(download_url):
    req = urllib.request.Request(download_url)
    req.set_proxy(PROXY_HOST, 'http')

    with urllib.request.urlopen(req) as read:
        return read.read()


def download(download_url, file=None):
    if not file:
        file = download_url.split('/')[-1]
    with open(file, 'wb') as f:
        f.write(get(download_url))


def main():
    download_url = 'http://series.uclv.cu/Ingles_1/Silicon%20Valley/Silicon%20Valley%20x%201/'
    req = urllib.request.Request(download_url)
    req.set_proxy(PROXY_HOST, 'http')

    response = urllib.request.urlopen(req)

    soup = BeautifulSoup(response.read(), features="html.parser")
    for a in soup.select('tr td a')[1:]:
        file = a.attrs.get('href')
        link = download_url + file
        if not os.path.isdir(DOWNLOAD_PATH):
            os.mkdir(DOWNLOAD_PATH)

        download(download_url=link, file=os.path.join(DOWNLOAD_PATH, file))


if __name__ == "__main__":
    url = 'http://series.uclv.cu/Ingles_1/Silicon%20Valley/Silicon%20Valley%20x%201/Silicon%20Valley%201x01%20480p%20hdtv%20x264-killers%20(1).mkv'
    download(url)
