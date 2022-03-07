from email import header
from urllib import response
import pytest
import requests
import json
from assertpy import assert_that

class TestApiMember():
    # ========= End point members ===========
    id_board    = '61fbdb90a57a185cd5c574c8'
    curl        = (f"https://api.trello.com/1/boards/{id_board}/memberships")
    headers     = {'Accept' : 'application/json'}
    query       = {'key' : '32f6e6037baed62c5b41befa51dcd4d6',
                   'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}

    # ======== End point add member =========
    idBoard     = '61fbdb90a57a185cd5c574c8'
    curl1       = (f"https://api.trello.com/1/boards/{idBoard}/members")
    queryParams = {'email' : 'diar96@gmail.com',
                   'fullName' : 'ardiansyah diar',
                   'type' : 'normal',
                   'key' : '32f6e6037baed62c5b41befa51dcd4d6',
                   'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}

    def test_get_member(self):
        response = requests.get(self.curl, params=self.query, headers=self.headers)

        assert_that(response.status_code).is_equal_to(200)
    
    def test_put_member(self):
        response = requests.put(self.curl1, params=self.queryParams)

        assert_that(response.status_code).is_equal_to(200)
        