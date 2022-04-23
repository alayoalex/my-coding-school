from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


try:
    html = urlopen('http://cubadebate.cu')
except HTTPError as e:
    print("The server returned an HTTP error")
except URLError as e:
    print("The server could not be found!")
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    allText = bs.find_all('span', {'class':{'comment_count'}})
    print(len(allText))
    print(type(allText))
    print(type(allText[50].child))
