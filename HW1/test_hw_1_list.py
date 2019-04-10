import pytest


class TestListClass:
    """Класс для проверки действий со списком с исп-м 2х фикстур"""
    @pytest.mark.usefixtures('second_fix', 'third_fix')
    def test_list_sum(self):
        """Проверка длины списка при сложении 2х списков"""
        list_1 = [1, 2, 3]
        list_2 = [4, 5, 6]
        sum_list = list_1 + list_2
        assert len(sum_list) == 6

    def test_list_add(self):
        """Проверка длины списка при добавлении элемента"""
        fruits = (['apple', 'pineapple', 'banana'])
        fruits.append('orange')
        fruits.append('lemon')
        assert len(fruits) == 5

    def test_list_ins(self):
        """Проверка изменения значения в списке"""
        test_list = [1, 2, 3, 4, 5, 6, 7, 8]
        test_list.insert(-2, 2)
        assert test_list.count(2) == 2
