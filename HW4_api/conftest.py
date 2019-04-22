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


@pytest.fixture()
def brew():
    client = API('https://api.openbrewerydb.org')
    return client


@pytest.fixture()
def cdnjs():
    client = API('https://api.cdnjs.com')
    return client
