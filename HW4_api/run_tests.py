""" Запуск теста """

import pytest


def test_start(additional_value):
    if additional_value == 'dog':
        test = [
            'test_api_dog.py'
        ]
    elif additional_value == 'brew':
        test = [
            'test_api_breweries.py'
        ]
    elif additional_value == 'cdnjs':
        test = [
            'test_api_cdnjs.py'
        ]
    elif additional_value == 'all':
        test = [
            'test_api_dog.py',
            'test_api_breweries.py',
            'test_api_cdnjs.py'
        ]
    else:
        print("Неверное название")

    pytest.main(test)

