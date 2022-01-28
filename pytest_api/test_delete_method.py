import requests
import json
import jsonpath
import pytest

def test_delete_method():

    url = 'https://api.trello.com/1/boards/61a0ec633d2a2664377695b1'

    query = {'key':'32f6e6037baed62c5b41befa51dcd4d6',
            'token': 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044',
            }
    
    response = requests.delete(url,params=query)

    code = response.status_code

    assert code

    json_response = json.loads(response.text)

    nilai = jsonpath.jsonpath(json_response,'_value')

    assert nilai[0] == None