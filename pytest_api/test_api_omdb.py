import requests
import json
import pytest


def test_api_omdb():

    url = 'http://www.omdbapi.com/'

    query = {'i' : 'tt3896198',
            'apikey' : '13e81452',
            't' : 'Iron man'}

    response_code = requests.get(url,params=query)

    code = response_code.status_code

    assert code == 200
