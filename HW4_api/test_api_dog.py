""" API tests for https://dog.ceo/dog-api/"""

import pytest
import requests


class API:
    def __init__(self, address):
        self.address = address

    def get(self, endpoint):
        url = "/".join((self.address, endpoint))
        return requests.get(url)


@pytest.fixture
def dog():
    client = API('https://dog.ceo/api')
    return client


ENDPOINTS = ['breeds/list/all',
             'breed/akita/images/random',
             'breeds/image/random',
             'breeds/image/random/51',
             'breed/hound/list',
             'breed/hound/images',
             'breed/hound/images/random',
             'breed/hound/images/random/3',
             'breed/hound/afghan/images',
             'breed/hound/afghan/images/random',
             'breed/hound/afghan/images/random/3']


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_all_endpoints(dog, endpoint):
    response = dog.get(endpoint)
    data = response.json()
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert data['message'] is not None


@pytest.mark.parametrize('endpoint', ENDPOINTS[3:4])
def test_random_im(dog, endpoint):
    """
    Test max value for DISPLAY MULTIPLE RANDOM IMAGES FROM ALL DOGS COLLECTION (max 50)
    """
    response = dog.get(endpoint)
    data = response.json()
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert len(data['message']) == 50
