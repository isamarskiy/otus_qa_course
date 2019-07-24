import pytest
import paramiko


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="127.0.1.1")
    parser.addoption("--port", action="store", default=int(22))
    parser.addoption("--user", action="store", default="root")
    parser.addoption("--passw", action="store", default="Qwerty12345")


@pytest.fixture(scope="function")
def client(request):
    host = request.config.getoption("--host")
    port = request.config.getoption("--port")
    user = request.config.getoption("--user")
    passw = request.config.getoption("--passw")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=passw, port=port)
    stdin, stdout, stderr = client.exec_command(request.param)
    data = stdout.read() + stderr.read()
    status = data.decode('utf-8').strip('\n')
    return status
