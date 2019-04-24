import pytest


def pytest_addoption(parser):
    parser.addoption('--additional_value', action='store', default='all')


@pytest.fixture(scope="session")
def additional_value(request):
    return request.config.getoption("--additional_value")
