from urllib.request import urlopen
from bs4 import BeautifulSoup

id = 4700
nombre = []
f = []
bs = []

for i in range(10):
    id += i
    f.append(urlopen("http://www.beisbolcubano.cu/SNBeisbol/general/atletas?id="+str(id)))
    bs.append(BeautifulSoup(f[i].read(), 'html.parser'))
    nombre.append(bs[i].find_all('span', {'class':'atl_datos'}))

for name in nombre:
    print(name)



