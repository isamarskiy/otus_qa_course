"""Запуск тестов с параметром. По умолчанию запуск всех тестов """
import pytest
import requests


class API:
    def __init__(self, address):
        self.address = address

    def get(self, endpoint):
        url = "/".join((self.address, endpoint))
        return requests.get(url)


def pytest_addoption(parser):
    parser.addoption(
        '--additional_value', action='store', default='all',
        help='Для запуска одного теста: dog, brew, cdnjs. Без аргумента запускаются все тесты'
    )


@pytest.fixture(scope="session")
def additional_value(request):
    return request.config.getoption("--additional_value")


@pytest.fixture
def dog():
    client = API('https://dog.ceo/api')
    return client


@pytest.fixture()
def cdnjs():
    client = API('https://api.cdnjs.com')
    return client


@pytest.fixture()
def brew():
    client = API('https://api.openbrewerydb.org')
    return client

