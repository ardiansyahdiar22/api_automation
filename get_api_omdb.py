import requests
import json

url = 'http://www.omdbapi.com/'

query = {'i' : 'tt3896198',
         'apikey' : '13e81452',
         't' : 'Iron man'}

response = requests.get(url,params=query)

print(response.status_code)

json_code = json.loads(response.text)
print(json_code)