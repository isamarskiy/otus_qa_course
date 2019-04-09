import pytest


@pytest.fixture()
def before(request):
    print('\nBEF_FIX STARTED')

    def end():
        print('\nBEF_FIX ENDED. ')

    request.addfinalizer(end)


@pytest.fixture(scope='session')
def first_fix(request):
    print('\nFIRST_FIX STARTED ')

    def end():
        print('\nFIRST_FIX ENDED.')

    request.addfinalizer(end)


@pytest.fixture(scope='module')
def second_fix(request):
    print('\nSECOND_FIX STARTED')

    def end():
        print('\nSECOND_FIX ENDED.')

    request.addfinalizer(end)


@pytest.fixture(scope='module')
def third_fix(request):
    print('\nTHIRD_FIX STARTED')

    def end():
        print('\nTHIRD_FIX ENDED.')

    request.addfinalizer(end)


@pytest.fixture()
def request_fix(request):
    print('\n-----------------')
    print('fixturename : %s' % request.fixturename)
    print('scope       : %s' % request.scope)
    print('function    : %s' % request.function.__name__)
    print('cls         : %s' % request.cls)
    print('module      : %s' % request.module.__name__)
    print('fspath      : %s' % request.fspath)
    print('-----------------')

    assert True
