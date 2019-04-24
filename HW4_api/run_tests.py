import pytest

fix_names = ['dog', 'brew', 'cdnjs', 'all']


def test_start(additional_value):
    for value in fix_names:
        if value == 'dog':
            test = ['test_api_dog.py']
        elif value == 'brew':
            test = ['test_api_breweries.py']
        elif value == 'cdnjs':
            test = ['test_api_cdnjs.py']
        elif value == 'all':
            test = ['test_api_dog.py', 'test_api_breweries.py', 'test_api_cdnjs.py']
        else:
            print("Неверное название")
            return

    pytest.main(test)
