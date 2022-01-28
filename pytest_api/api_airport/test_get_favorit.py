import json
from pydoc import resolve
import re
from urllib import response
import requests
import pytest

def test_get_fav_all():
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    url = ('https://airportgap.dev-tester.com/api/favorites')

    response = requests.get(url, headers=auth)
    print(response.text)
    assert response.status_code == 200

def test_get_fav_id():
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    airport_id = "4063"
    url = (f"https://airportgap.dev-tester.com/api/favorites/{airport_id}")

    response = requests.get(url, headers=auth)
    assert response.status_code == 200
    data = response.json().get("data") # <== Parsing data from JSON
    assert data["id"] == "4063" 
    assert data["attributes"]["airport"]["country"] == "Greenland"

def test_get_fav_not_found():
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    airport_id = "4052"
    url = (f"https://airportgap.dev-tester.com/api/favorites/{airport_id}")

    response = requests.get(url, headers=auth)
    assert response.status_code == 404
    assert response.text

     