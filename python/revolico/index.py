import requests

res = requests.get('https://www.revolico.com/vivienda/compra-venta')

# print(res.text)
# print('\n')
print(res.ok)
print(res.reason)
print(res.links)
