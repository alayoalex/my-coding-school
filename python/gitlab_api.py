# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://gitlab.com/api/v4/projects/43783535/variables"

# auth = HTTPBasicAuth("alexei.alayo@sivah.net", "ATATT3xFfGF0Od4q6cVPyUm_kti5-J2HUdOUwXFjZEf12ybN62Ady8qDj1D5Rgu0r2bfBB0llDFbQKBG65AZ7bjsIYoyey0IzhZ4cuj2uDzN6kVxN9ZagkqO1OlDKcF22gJ-5PeYbxAWnsUGhqkSzfNDR46ekGUj0VigjPcItkij2r3_z_9cZ38=036F5A82")

headers = {
  "Accept": "application/json",
  "PRIVATE-TOKEN": "glpat-zcccccccccccccccccccccccccccc"
}

response = requests.request(
   "GET",
   url,
   headers=headers
#    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

for r in response.json():
    print(r['name'])
