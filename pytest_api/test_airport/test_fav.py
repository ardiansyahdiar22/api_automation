import imp
from msilib.schema import Class
from urllib import response
import requests
import json
import pytest
from assertpy import assert_that

class TestFavorite():
    auth = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    url = ('https://airportgap.dev-tester.com/api/favorites')

    def _get_first_favorite(self):
        response_id = requests.get(self.url, headers=self.auth)
        return response_id.json().get('data')[0].get('id')

    def test_create(self):
        query = {'airport_id' : 'GKA', 'note' : 'Tambah favorit'}
        response = requests.post(self.url, headers=self.auth, params=query)

        assert_that(response.status_code).is_equal_to(201)
        json_code = response.json().get('data')
        assert_that(json_code['attributes']['airport']['name']).is_equal_to('Goroka Airport')
        assert_that(json_code['attributes']['airport']['country']).is_equal_to('Papua New Guinea')
        print(response.text)
    
    def test_get_fav(self):
        response = requests.get(self.url, headers=self.auth)

        assert_that(response.status_code).is_equal_to(200)
        print(response.text)
        assert_that(len(response.json().get('data'))).is_greater_than_or_equal_to(1)
    
    def test_edit_note(self):
        airport_id = self._get_first_favorite()
        query = {'note' : 'Edit catatan yah boskuh'}
        response = requests.patch(f"{self.url}/{airport_id}", headers=self.auth, params=query)

        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()['data']['attributes']['note']).is_equal_to('Edit catatan yah boskuh')

    def test_delete_fav(self):
        airport_id = self._get_first_favorite()
        response = requests.delete(f"{self.url}/{airport_id}", headers=self.auth)

        assert_that(response.status_code).is_equal_to(204)