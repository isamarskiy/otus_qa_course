import pytest


@pytest.mark.usefixtures("before")
def test_tuple_add():
        """Проверка сложения кортежей"""
        test_tuple_1 = ('one', 'two', 'three', 'four', 'five')
        test_tuple_2 = ('six', 'seven', 'eight', 'nine', 'ten')
        sum_tuples = test_tuple_1 + test_tuple_2
        assert sum_tuples == ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
        return sum_tuples


@pytest.mark.usefixtures("before")
def test_tuple_in():
    """Копирование кортежа и проверка элемента с индексом 7"""
    new_test_tuple = test_tuple_add()
    assert new_test_tuple[7] == 'eight'
