import imp
import pytest
import requests
import json
import jsonpath
from assertpy import assert_that

class TestPutList():
    idList = '6214f20157b71080f8a6d663'
    curl = (f"https://api.trello.com/1/lists/{idList}")
    query = {'name' : 'edit list lagi yaa',
             'key' : '32f6e6037baed62c5b41befa51dcd4d6',
             'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}
    
    def test_put(self):
        response = requests.put(self.curl, params=self.query)

        assert_that(response.status_code).is_equal_to(200)
        json_code = json.loads(response.text)
        code = jsonpath.jsonpath(json_code, 'name')
        assert_that(code[0]).is_equal_to('edit list lagi yaa')