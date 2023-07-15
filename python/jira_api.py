# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://isyndeo.atlassian.net/rest/api/2/search"

auth = HTTPBasicAuth(
    "alexei.alayo@sivah.net", 
    "ATATT3xFfGF0Od4q6cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx2gJ-5PeYbxAWnnnnnnnnnnnnnnnnnnnnnnnnnnnkij2r3_z_9cZ38=036F5A82"
)

headers = {
  "Accept": "application/json"
}

query = {
  'jql': 'project = "iCore R.C.M" AND status = "Ready for Prod"'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

for res in response.json()['issues']:
    # if res['fields']['status']['name'] == "Ready for Sprint":
    print(res['fields']['status']['name'])
