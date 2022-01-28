import json
from urllib import response
import requests
import pytest

# # def test_delete_by_id():
#     auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
#     airport_id = "4056"
#     url = (f"https://airportgap.dev-tester.com/api/favorites/{airport_id}")

#     response = requests.delete(url, headers=auth)
#     assert response.status_code == 204

def test_delete_all():
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    url = ("https://airportgap.dev-tester.com/api/favorites/clear_all")

    response = requests.delete(url, headers=auth)
    assert response.status_code == 204