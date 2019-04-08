import pytest


@pytest.fixture()
def before():
    print('\nНачало теста')


def test_eval_num(before):
    assert (2+2)*2 == 8


def test_sum_string(before):
    # Check sum of 2 strings
    str_val_1 = 'Hi'
    str_val_2 = ' Jack'
    assert str_val_1 + str_val_2 == 'Hi Jack'

class TestListClass:
    def test_list_sum(self):
        # Check sum of 2 lists
        list_1 = [1, 2, 3]
        list_2 = [4, 5, 6]
        sum_list = list_1 + list_2
        assert len(sum_list) == 6

    def test_list_add(self):
        # Check set length after adding a new element
        fruits = (['apple', 'pineapple', 'banana'])
        fruits.append('orange')
        fruits.append('lemon')
        assert len(fruits) == 5

    def test_list_ins(self):
        # Замена значения в списке
        test_list = [1, 2, 3, 4, 5, 6, 7, 8]
        test_list.insert(-2, 2)
        assert test_list.count(2) == 2


def test_dict_add():
    # Проверка корретного добавления элемента в словарь (пример с чисткой словаря?) или добавление элемента в удаленный
    # словарь
    dict_clubs = {'Spain': 'Barcelona', 'Italy': 'Juventus', 'England' : 'Arsenal'}
    dict_clubs['Russia'] = 'Zenit'
    dict_clubs['Holland'] = 'AZ'
    dict_clubs.clear()
    assert dict_clubs == {}


def test_dict_num2():
    # Создание словаря и проверка элемента с индексом 3
    test_dict = {a: a ** 2 for a in range(5)}
    assert list(test_dict.items())[3] == (3, 9)


def test_set_intersection():
    # Разница 2х списков
    test_set_1 = {'dog', 'cat', 'cow', 'duck', 'horse'}
    test_set_2 = {'horse', 'puppy', 'kitten', 'cow', 'duck'}
    inter = test_set_1.intersection(test_set_2)
    assert inter == test_set_1.intersection(test_set_2)


def test_set_copy():
    # Проверка копирования множества
    test_set_1 = {'dog', 'cat', 'cow', 'duck', 'horse'}
    test_set_2 = test_set_1.copy()
    assert test_set_2 == test_set_1


def test_tuple_add():
    # Сложение кортежей и проверка значения индекса (почему индекс 7 возвращает eight?)
    test_tuple_1 = ('one', 'two', 'three', 'four', 'five')
    test_tuple_2 = ('six', 'seven', 'eight', 'nine', 'ten')
    sum_tuples = test_tuple_1 + test_tuple_2
    assert sum_tuples == ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
    return sum_tuples


def test_tuple_in():
    new_test_tuple = test_tuple_add()
    assert new_test_tuple[7] == 'eight'
