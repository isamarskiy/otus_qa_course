import pytest


def test_eval_num(before):
    """Проверка сложения и умножения с фикстурой before"""
    assert (2+2)*2 == 8


############################################
def test_sum_string(first_fix):
    """Проверка сложения строк с исп. фикстуры first_fix"""
    str_val_1 = 'Hi'
    str_val_2 = ' Jack'
    assert str_val_1 + str_val_2 == 'Hi Jack'
############################################


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


def test_dict_add(before):
    """Проверка очистки словаря после добавления элеменента"""
    dict_clubs = {'Spain': 'Barcelona', 'Italy': 'Juventus', 'England' : 'Arsenal'}
    dict_clubs['Russia'] = 'Zenit'
    dict_clubs['Holland'] = 'AZ'
    dict_clubs.clear()
    assert dict_clubs == {}


def test_dict_num2(before):
    """Создание словаря и проверка элемента с выбранным индексом"""
    test_dict = {a: a ** 2 for a in range(5)}
    assert list(test_dict.items())[3] == (3, 9)


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
