import requests
import pytest

def test_method_get():
    url = 'https://reqres.in/api/users/2'
    
    response = requests.get(url)

    code = response.status_code
    assert code == 200