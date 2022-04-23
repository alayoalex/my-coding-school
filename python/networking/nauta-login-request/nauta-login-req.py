import requests
import urllib.request

#with urllib.request.urlopen('https://secure.etecsa.net:8443/') as response:
 #   html = response.read()

#print(html)

session = requests.Session()

params = {'username': 'aalayo2015@nauta.com.cu', 'password': 'Melquisedec12*'}

s = session.post('https://secure.etecsa.net:8443/', params)

print('Cookie is set to:')
print(s.cookies.get_dict())
print('Going to profile page...')

s = session.get('https://secure.etecsa.net:8443/nauta_etecsa//OnlineURL/pc_index.jsp', cookies=s.cookies)
print(s.text)
