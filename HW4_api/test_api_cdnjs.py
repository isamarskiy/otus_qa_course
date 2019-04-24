""" API tests for https://cdnjs.com/api"""
import pytest
import requests


class API:
    def __init__(self, address):
        self.address = address

    def get(self, endpoint):
        url = "/".join((self.address, endpoint))
        return requests.get(url)


@pytest.fixture()
def cdnjs():
    client = API('https://api.cdnjs.com')
    return client


ENDPOINTS = ['libraries',
             'libraries?output=human',
             'libraries/jquery',
             'libraries?search=jquery&output=human',
             'libraries?search=ractive',
             'libraries?search=ractive&fields=version,description',
             'libraries?search=ractive&output=human&fields=version,description',
             'libraries?search=1140&fields=assets',
             'libraries?search=1140&fields=assets&output=human']


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_all_endpoints(cdnjs, endpoint):
    response = cdnjs.get(endpoint)
    assert response.status_code == 200
    assert response.reason == 'OK'


@pytest.mark.parametrize('endpoint', ENDPOINTS[2:3])
def test_some_lib(cdnjs, endpoint):
    response = cdnjs.get(endpoint)
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == 'jquery'
