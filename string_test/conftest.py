import pytest


@pytest.fixture(scope='function')
def bef_str(request):
    print('\nStart test for string')

    def aft_string():
        print('\nTest finished')

    request.addfinalizer(aft_string)


@pytest.fixture(scope='session')
def bef_dict(request):
    print('\nStart test for dict')

    def aft_string():
        print('\nTest finished')

    request.addfinalizer(aft_string)


@pytest.fixture(scope='module')
def bef_list(request):
    print('\nStart test for list')

    def aft_list():
        print('\nTest finished')

    request.addfinalizer(aft_list)


@pytest.fixture(scope='module')
def sec_list_fix(request):
    print('\nStart second fixture test for list')

    def aft_sec_fix():
        print('\nTest finished')

    request.addfinalizer(aft_sec_fix)
