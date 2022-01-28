import json
import queue
from wsgiref import headers
import requests

url = ('https://airportgap.dev-tester.com/api/favorites') 

headers = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}

paramsQuery = {
    "airport_id" : "LAE",
    "note" : "Test API"
}

response = requests.post(url,headers=headers,params=paramsQuery)
print(response.status_code)

json_code = json.loads(response.text)
print(json_code)

