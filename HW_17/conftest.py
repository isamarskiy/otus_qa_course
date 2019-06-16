import os
import pkgutil
import pytest


@pytest.fixture(scope='session')
def packages():
    packages_list = []
    for package in pkgutil.iter_modules():
        packages_list.append(package.name)
    return packages_list


@pytest.mark.usefixtures("packages")
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, packages):
    request.config._metadata.update(
        {"env_var": os.environ,
         "packages": packages}
    )
    yield

