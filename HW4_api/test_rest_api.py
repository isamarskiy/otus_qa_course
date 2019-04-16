import pytest
import requests
import json

url_main = ('https://dog.ceo/api/breeds/list/all', 'https://dog.ceo/api/breed/akita/images/random')
url_random_im = ('https://dog.ceo/api/breeds/image/random', 'https://dog.ceo/api/breeds/image/random/3')
url_by_breed = ('https://dog.ceo/api/breed/hound/images', 'https://dog.ceo/api/breed/hound/images/random',
                'https://dog.ceo/api/breed/hound/images/random/3')
url_by_sub_breed = ('https://dog.ceo/api/breed/hound/afghan/images',
                    'https://dog.ceo/api/breed/hound/afghan/images/random',
                    'https://dog.ceo/api/breed/hound/afghan/images/random/3')
urls = [url_main, url_random_im, url_by_breed, url_by_sub_breed]


@pytest.fixture(params=url_main)
def test_fixture(request):
    print(request.param)
    return requests.get(request.param)


@pytest.mark.usefixtures('test_fixture')
def test_resp(test_fixture):
    status_mes = test_fixture.json()
    assert test_fixture.status_code == 200
    assert status_mes['status'] == 'success'



"""
r = json.loads(a.text)
len(r['message'])
"""