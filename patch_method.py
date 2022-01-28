from email import header
import json
from wsgiref import headers
import requests

url = ('https://airportgap.dev-tester.com/api/favorites/4057')

headers = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}

query = {'note' : 'edit yaaa lagi yaa'}

response = requests.patch(url,headers=headers,params=query)
print(response.status_code)

json_code = json.loads(response.text)
print(json_code)

