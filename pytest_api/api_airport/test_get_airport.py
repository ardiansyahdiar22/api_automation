import json
from pydoc import resolve
import re
from urllib import response
import requests
import pytest

def test_get_data_by_id():
    airport_id = "MAG"
    response = requests.get(f"https://airportgap.dev-tester.com/api/airports/{airport_id}")
    
    assert response.status_code == 200
    data = response.json().get('data')
    assert data['id'] == 'MAG'
    assert data['attributes']['name'] == "Madang Airport"
    assert data["attributes"]["icao"] == "AYMD"

def test_get_data():
    response = requests.get('https://airportgap.dev-tester.com/api/airports/')
    assert response.status_code == 200
    assert len(response.json().get('data')) == 30

def test_not_found():
    airport_id = 'juanda'
    response = requests.get(f"https://airportgap.dev-tester.com/api/airports/{airport_id}")

    assert response.status_code == 404
    assert response.text