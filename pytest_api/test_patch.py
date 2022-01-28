import json
from pickle import FALSE
from urllib import response
from wsgiref import headers
import pytest
import requests
import jsonpath
from assertpy import assert_that

def test_patch():
    url = ('https://airportgap.dev-tester.com/api/favorites/4058')
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}

    query = {'note' : 'edit yah'}

    response = requests.patch(url, headers=auth, params=query)

    code = response.status_code
    assert code == 200

    json_code = json.loads(response.text)
    notes = jsonpath.jsonpath(json_code, 'note')
    print(json_code)

    assert notes == False
