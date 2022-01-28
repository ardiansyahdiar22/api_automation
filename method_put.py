import requests
import json

url = 'https://api.trello.com/1/boards/61acba19eca611868c4a9627'

query = {'key':'32f6e6037baed62c5b41befa51dcd4d6',
        'token': 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044',
        'name' : 'update board with python'}

response = requests.put(url, params=query)
print(response.status_code)

json_code = json.loads(response.text)
print(json_code)