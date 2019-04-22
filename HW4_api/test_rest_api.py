""" API tests for https://dog.ceo/dog-api/"""

import pytest

Endpoints = ['breeds/list/all',
             'breed/akita/images/random',
             'breeds/image/random',
             'breeds/image/random/3',
             'breed/hound/images',
             'breed/hound/images/random',
             'breed/hound/images/random/3',
             'breed/hound/afghan/images',
             'breed/hound/afghan/images/random',
             'breed/hound/afghan/images/random/3']


@pytest.mark.parametrize('endpoint', Endpoints)
def test_all_endpoints(dog, endpoint):
    response = dog.get(endpoint)
    status_mes = response.json()
    assert response.status_code == 200
    assert status_mes['status'] == 'success'
#добавить проверку message
#добавить проверку в методе с 50ю значениями