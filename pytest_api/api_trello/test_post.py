import json
import requests
import pytest
from assertpy import assert_that
import jsonpath

class TestPostMethod():
    curl = ('https://api.trello.com/1/boards/')
    query = {'name' : 'test add automation', 
    'key' : '32f6e6037baed62c5b41befa51dcd4d6', 
    'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}

    def test_post(self):
        response = requests.post(self.curl, params=self.query)

        assert_that(response.status_code).is_equal_to(200)
        json_code = json.loads(response.text)
        code = jsonpath.jsonpath(json_code,'name')
        assert_that(code[0]).is_equal_to('test add automation')