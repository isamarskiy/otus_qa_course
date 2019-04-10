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
