import pytest


@pytest.mark.usefixtures("request_fix")
class TestSetClass:
    def test_set_intersection(self):
        """Проверка совпадения в 2х множествах"""
        test_set_1 = {'dog', 'cat', 'cow', 'duck', 'horse'}
        test_set_2 = {'horse', 'puppy', 'kitten', 'cow', 'duck'}
        inter = test_set_1.intersection(test_set_2)
        assert inter == {'horse', 'cow', 'duck'}

    def test_set_copy(self):
        """Проверка копирования множества"""
        test_set_1 = {'dog', 'cat', 'cow', 'duck', 'horse'}
        test_set_2 = test_set_1.copy()
        assert test_set_2 == test_set_1
