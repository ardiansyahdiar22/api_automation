from urllib import response
import pytest
import requests
import json
from assertpy import assert_that

class TestApiMove():
    # ============ Move list ================
    idList = '62139bad61d5385fc9fd2b00'
    curl = (f"https://api.trello.com/1/lists/{idList}/idBoard") 
    query = {'value' : '61fbe97f163cda02d16de67c',
             'key' : '32f6e6037baed62c5b41befa51dcd4d6',
             'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}

    # ============= Move card ================
    id = '6214e26d4f1f127313ad1d9f'
    curl1 = (f"https://api.trello.com/1/lists/{id}/moveAllCards")
    queryParams = {'idBoard' : '61a0e365a451a3124bc3095d',
                   'idList' : '61a0e365a451a3124bc3095f',
                   'key' : '32f6e6037baed62c5b41befa51dcd4d6',
                   'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}

    def test_api_move(self):
        response = requests.put(self.curl, params=self.query)

        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()['name']).is_equal_to('list board test')
        print(response.text)

    def test_api_move_card(self):
        response = requests.post(self.curl1, params=self.queryParams)

        assert_that(response.status_code).is_equal_to(200)
        