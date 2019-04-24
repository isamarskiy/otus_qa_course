""" API tests for https://www.openbrewerydb.org/"""

import pytest

ENDPOINTS = ['breweries',
             'breweries?by_state=new_york',
             'breweries?by_name=cooper',
             'breweries/5494',
             'breweries?by_tag=patio',
             'breweries?by_name=cooper&by_state=new_york',
             'breweries?by_state=ohio&sort=type,-name',
             'breweries?page=2&per_page=30',
             'breweries/autocomplete?query=dog',
             'breweries/search?query=dog']


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_all_endpoints(brew, endpoint):
    response = brew.get(endpoint)
    assert response.status_code == 200
    assert response.json() is not None


@pytest.mark.parametrize('endpoint', ENDPOINTS[2:3])
def test_api_by_tag(brew, endpoint):
    response = brew.get(endpoint)
    #data = response.json()
    assert response.status_code == 200
    assert response.reason == 'OK'
    #assert data['tag_list']['patio'] == ['patio']


@pytest.mark.parametrize('endpoint', ENDPOINTS[3:4])
def test_get_brew(brew, endpoint):
    """by brew id"""
    response = brew.get(endpoint)
    check = response.json()
    assert response.status_code == 200
    assert check['id'] == 5494
