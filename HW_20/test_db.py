from pymysql.err import DatabaseError, DataError
import pymysql
import pytest

new_row_name = 'Latvian'


@pytest.fixture(scope='module')
def db_connect():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='bn_opencart',
        db='bitnami_opencart',
        port=4407)
    yield connection
    connection.commit()
    connection.close()


@pytest.fixture
def cursor(db_connect):
    cursor = db_connect.cursor()
    yield cursor
    cursor.close()


def test_create_new_row(cursor):
    """ Добавление новой записи в таблицу oc_language"""
    try:
        query = """
        insert into oc_language
        values ('', %s,'ru-ru', 'ru-RU,ru_RU.UTF-8,ru_RU', 'gb.png', 'russian', 1, 1)
        """
        cursor.execute(query, new_row_name)
    except DatabaseError as err:
        print("Error: ", err)


def test_check_new_row(cursor):
    """ Проверка наличия добавленной записи в таблице oc_language"""
    try:
        query = """select * from oc_language where name = %s;"""
        cursor.execute(query, new_row_name)
        result = cursor.fetchone()
        row = result[1]
        assert new_row_name in row
    except DataError as err:
        print("Error: ", err)
