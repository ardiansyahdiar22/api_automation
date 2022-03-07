from email import header
from urllib import response
import requests
import json
import jsonpath
import pytest
from assertpy import assert_that

class TestApiAttachment():
    idCard = '621650fac848ce54d7c7c970'
    curl  = (f"https://api.trello.com/1/cards/{idCard}/attachments")
    headers = {"Accept": "application/json"}

    def test_create(self):
        query = {'name' : 'attachment bug 1',
                 'url' : 'https://drive.google.com/file/d/1aiNNckQQjq-363o0Tm-GTF8Qk68ms1a9/view?usp=sharing',
                 'key' : '32f6e6037baed62c5b41befa51dcd4d6',
                 'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}

        response = requests.post(self.curl, params=query, headers=self.headers)

        assert_that(response.status_code).is_equal_to(200)
        json_code = json.loads(response.text)
        code = jsonpath.jsonpath(json_code, 'name')
        assert_that(code[0]).is_equal_to('attachment bug 1')
    
    def test_get(self):
        query = {'key' : '32f6e6037baed62c5b41befa51dcd4d6',
                 'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}
        
        response = requests.get(self.curl, params=query, headers=self.headers)
        
        assert_that(response.status_code).is_equal_to(200)
    
    