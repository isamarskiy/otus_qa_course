""" API tests for https://cdnjs.com/api"""
import pytest

urls = ['/libraries',
        'https://api.cdnjs.com/libraries?output=human',
        'libraries/jquery',
        'libraries?search=jquery&output=human',
        'libraries?search=ractive',
        'libraries?search=ractive&fields=version,description',
        'libraries?search=ractive&output=human&fields=version,description',
        'libraries?search=1140&fields=assets',
        'libraries?search=1140&fields=assets&output=human']


@pytest.mark.parametrize('endpoint',urls)
def test_all_endpoints(cdnjs, endpoint):
    response = cdnjs.get(endpoint)
    #check_json = response.json()
    assert response.status_code == 200
    assert response.json() is not None

'''
#check name for https://api.cdnjs.com/libraries/jquery'
check name for https://api.cdnjs.com/libraries?search=ractive
check specific fields for https://api.cdnjs.com/libraries?search=ractive&fields=version,description
check specific fields for https://api.cdnjs.com/libraries?search=ractive&output=human&fields=version,description
check assets for https://api.cdnjs.com/libraries?search=1140&fields=assets
'''