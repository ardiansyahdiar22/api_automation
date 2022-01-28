import requests
import pytest
import json
import jsonpath

def test_method_post():
    url = 'https://api.trello.com/1/boards/'

    query = {'key'  : '32f6e6037baed62c5b41befa51dcd4d6',
             'token': 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044',
             'name' : 'add board with pytest'}

    response = requests.post(url,params=query)

    code = response.status_code

    assert code == 200

    json_code = json.loads(response.text)

    name = jsonpath.jsonpath(json_code,'name')

    assert name[0] == 'add board with pytest'