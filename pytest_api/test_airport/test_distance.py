import imp
import json
import queue
import requests
import pytest
from assertpy import assert_that


class TestAddDistance():
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    curl = ('https://airportgap.dev-tester.com/api/airports/distance')

    def testAddDistance(self):
        query = {'from' : 'POM', 'to' : 'UAK'}
        response = requests.post(self.curl, headers=self.auth, params=query)

        assert_that(response.status_code).is_equal_to(200)
        json_code = response.json().get('data')
        assert_that(json_code['id']).is_equal_to('POM-UAK')