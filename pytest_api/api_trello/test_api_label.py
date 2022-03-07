from urllib import response
from webbrowser import get
import requests
import json
import pytest
import jsonpath
from assertpy import assert_that

class TestApiLabel():
    curl = ('https://api.trello.com/1/labels')

    def _get_first_label(self):
        labels_id = requests.get(self.curl)
        json_code = json.loads(labels_id.text)
        return json_code.get('id')
        
    def test_create(self):
        query = {'name' : 'label ketiga',
                'color' : 'green',
                'idBoard' : '619f07cddf0cb7483859bafe',
                'key' : '32f6e6037baed62c5b41befa51dcd4d6',
                'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}
        
        response = requests.post(self.curl, params=query)

        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()['name']).is_equal_to('label ketiga')
        assert_that(response.json()['color']).is_equal_to('green')
        print(response.text)

    def test_get(self):
        id_label = self._get_first_label()
        query = {'key' : '32f6e6037baed62c5b41befa51dcd4d6',
                'token' : 'd7402af4d4605d60c425b50ba0347c46b7ed5a7f1f0e94f39d66bc839d60c044'}
        
        response = requests.get(f"{self.curl}/{id_label}", params=query)

        assert_that(response.status_code).is_equal_to(200)