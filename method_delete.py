import requests
import json

url = 'https://api.trello.com/1/boards/61a0e4590215598eea10d0d3'

query = {'key':'32f6e6037baed62c5b41befa51dcd4d6',
        'token': 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044',
        }

# cetak respon json
response = requests.delete(url,params=query)
print(response.status_code)

# menampilkan data json
json_response = json.loads(response.text)
print(json_response)
