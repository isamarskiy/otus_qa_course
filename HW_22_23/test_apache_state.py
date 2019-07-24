import pytest


@pytest.mark.parametrize('client', ['systemctl is-active apache2.service'], indirect=True)
def test_apache_status(client):
    status = client
    print(status)
    if status == 'active':
        assert True
    else:
        assert False


@pytest.mark.parametrize('client', ['systemctl stop apache2.service'], indirect=True)
def test_apache_stop(client):
    status = client
    print(status)
    if status == 'inanctive':
        assert True
    else:
        assert False


@pytest.mark.parametrize('client', ['systemctl start apache2.service'], indirect=True)
def test_apache_start(client):
    status = client
    print(status)
    if status == 'active':
        assert True
    else:
        assert False


@pytest.mark.parametrize('client', ['systemctl is-active mysql.service'], indirect=True)
def test_mysql_status(client):
    status = client
    print(status)
    if status == 'active':
        assert True
    else:
        assert False


@pytest.mark.parametrize('client', ['systemctl stop mysql.service'], indirect=True)
def test_mysql_stop(client):
    status = client
    print(status)
    if status == 'inanctive':
        assert True
    else:
        assert False


@pytest.mark.parametrize('client', ['systemctl start mysql.service'], indirect=True)
def test_mysql_start(client):
    status = client
    print(status)
    if status == 'active':
        assert True
    else:
        assert False
