import imp
from pickletools import read_uint1
from urllib import response
import requests
import pytest
import json
import jsonpath
from assertpy import assert_that

class TestApiCard():
    id = '62165149b88ba46ac8dd5546'
    curl = (f"https://api.trello.com/1/cards/{id}")
    headers = {"Accept": "application/json"}
        
    def test_get_card(self):
        query = {'key' : '32f6e6037baed62c5b41befa51dcd4d6', 
                'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}

        response = requests.get(self.curl, params=query, headers=self.headers)

        assert_that(response.status_code).is_equal_to(200)
    
    def test_put_card(self):
        query = {'name' : 'Ticket bug hari ini 24 Feb 2022',
                'key'   : '32f6e6037baed62c5b41befa51dcd4d6', 
                'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}
        
        response = requests.put(self.curl, params=query, headers=self.headers)

        assert_that(response.status_code).is_equal_to(200)
        json_code = json.loads(response.text)
        code = jsonpath.jsonpath(json_code, 'name')
        assert_that(code[0]).is_equal_to('Ticket bug hari ini 24 Feb 2022')
    
    # def test_delete_card(self):
    #     query = {'key' : '32f6e6037baed62c5b41befa51dcd4d6', 
    #             'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}
        
    #     response = requests.delete(self.curl, params=query)

    #     assert_that(response.status_code).is_equal_to(200)