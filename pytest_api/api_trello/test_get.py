import imp
import json
import requests
import pytest
from assertpy import assert_that

class TestGetMethod():
    curl = ('https://api.trello.com/1/boards/SV3wz5hV')
    query = {'key' : '32f6e6037baed62c5b41befa51dcd4d6', 'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}

    def test_get(self):
        response = requests.get(self.curl, params=self.query)

        assert_that(response.status_code).is_equal_to(200)
        
        