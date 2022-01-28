import imp
from typing import ParamSpecArgs
import requests
import json
import pytest

def test_patch():
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    aiport_id = "4066"
    url = (f"https://airportgap.dev-tester.com/api/favorites/{aiport_id}")

    query = {'note' : 'Edit catatan lagi 2'}

    response = requests.patch(url, headers=auth, params=query)
    assert response.status_code == 200
    json_code = response.json().get("data")
    assert json_code["attributes"]["note"] == 'Edit catatan lagi 2'

def test_negatif():
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    aiport_id = "20"
    url = (f"https://airportgap.dev-tester.com/api/favorites/{aiport_id}")

    query = {'note' : 'Edit catatan'}

    response = requests.patch(url, headers=auth, params=query)
    assert response.status_code == 404