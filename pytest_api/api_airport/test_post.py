from urllib import response
from wsgiref.util import request_uri
import requests
import json
import pytest

def test_post_distance():
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    url = ('https://airportgap.dev-tester.com/api/airports/distance')

    query = {'from' : 'HGU', 'to' : 'LAE'}

    response = requests.post(url, headers=auth, params=query)
    assert response.status_code == 200
    data = response.json().get("data")
    assert data["id"] == "HGU-LAE"

def test_post_favorite():
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    url = ('https://airportgap.dev-tester.com/api/favorites')

    query = {'airport_id' : 'POM', 'note' : 'Tambah favorit'}

    response = requests.post(url, headers=auth, params=query)
    assert response.status_code == 201
    data = response.json().get("data")
    assert data["attributes"]["airport"]["name"] == "Port Moresby Jacksons International Airport"