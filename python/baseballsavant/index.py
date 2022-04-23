import requests

res = requests.get('https://baseballsavant.mlb.com/leaderboard/statcast')

print(res.text)
print('\n')
print(res.links)
