""" API tests for https://www.openbrewerydb.org/"""

import pytest
import json
import time

Endpoints = ['breweries',
             'breweries?by_state=new_york',
             'breweries?by_name=cooper',
             'breweries?by_tag=patio',
             'breweries?by_name=cooper&by_state=new_york',
             'breweries?by_state=ohio&sort=type,-name',
             'breweries?page=2&per_page=30',
             'breweries/5494',
             'breweries/autocomplete?query=dog',
             'breweries/search?query=dog']

Endpoint_by_state = 'breweries?by_state=new_york'
Endpoint_by_name = 'breweries?by_name=cooper'


@pytest.mark.parametrize('endpoint', Endpoints)
def test_all_endpoints(brew, endpoint):
    response = brew.get(endpoint)
    #check_json = response.json()
    assert response.status_code == 200
    assert response.json() is not None


@pytest.mark.parametrize('endpoint', Endpoint_by_state)
def test_endpoint_by_name(brew, endpoint):
    response = brew.get(Endpoint_by_state)
    check = response.json()
    assert response.status_code == 200
    assert check['State'] == 'New York'


@pytest.mark.parametrize('endpoint)



#Pagination & Per Page - проверка
#рассмотреть возможность проверки в условиях
#

'''
проверка атрибута фильтра (отдельная фикстура)
по стейту
14 атрибутов в json'е
Pagination & Per Page - проверка
рассмотреть возможность проверки в условиях
'''