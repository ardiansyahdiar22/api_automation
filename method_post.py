import requests
import json

url = 'https://api.trello.com/1/boards/'

query = {'key':'32f6e6037baed62c5b41befa51dcd4d6',
        'token': 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044',
        'name' : 'add new board'
}

response = requests.post(url,params=query)

print(response.status_code)

json_code = json.loads(response.text)
print(json_code)