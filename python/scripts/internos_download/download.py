import os
import re
import threading
import urllib
import urllib3
import requests

from bs4 import BeautifulSoup
from clint.textui import progress

PROJECT_DIR = os.path.dirname(os.path.realpath('internos_download'))
DOWNLOAD_PATH = os.path.join(PROJECT_DIR, 'downloads')
urllib3.disable_warnings()

def synchronized(lock):
    def dec(f):
        def func_dec(*args, **kwargs):
            lock.acquire()
            try:
                return f(*args, **kwargs)
            finally:
                lock.release()

        return func_dec

    return dec


class DownloadThread(threading.Thread):
    downloadlock = threading.Lock()

    def __init__(self, url, path):
        threading.Thread.__init__(self)
        self.url = url
        self.path = path

    @synchronized(downloadlock)
    def run(self):
        self.download(url=self.url, path=self.path)

    def download(self, url, path):
        response = requests.get(url, verify=False, stream=True)
        if response.status_code == 200:
            total_length = int(response.headers.get('content-length'))
            print('url: (%s) Tamaño: %.2f MB' % (url, (total_length / 1048576)))
            with open(path, 'wb') as file:
                chunk_size = 1024 * 1024
                for chunk in progress.bar(it=response.iter_content(chunk_size=chunk_size) ,
                                          label='Size %.2f MB:' % (total_length / 1048576) ,
                                          expected_size=(total_length / chunk_size)):
                    if chunk:
                        file.write(chunk)
                file.flush()


def main(url, download_path):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, features="html.parser")

    title = soup.select_one('section#post-content h1.page-title').text
    descargar = input('Desea descargar "%s" (yes|no) [default: yes]' % title)
    descargar = True if descargar == '' or descargar == 'yes' or descargar == 'y' else False

    links = [a.attrs.get('href') for a in
             soup.select('div.media-info div.media-actions li.download a[href^=/archivo_multimedia]')]
    names = [str(a.text).strip() for a in soup.select('div.media-info h4.media-title a.titulo-mini')]

    links.reverse()
    names.reverse()

    for i in range(0, len(links)):
        matches = re.match(r'(.*)url=(.*)&nid=(.*)$', links[i])
        fileurl = urllib.parse.unquote(matches.group(2))
        filename = re.match(r'(.*):80/(.*)$', fileurl).group(2)
        if descargar:
            if not os.path.isdir(download_path):
                os.mkdir(download_path)
            filepath = os.path.join(download_path, filename)

            download = DownloadThread(url=fileurl, path=filepath)
            download.start()


if __name__ == '__main__':
    url = input('URL >> ')
    path = input("Directorio a guardar [default: %s] >> " % DOWNLOAD_PATH)
    download_path = path if path else DOWNLOAD_PATH
    main(url=url, download_path=download_path)
