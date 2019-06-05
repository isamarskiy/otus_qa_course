import os
from urllib.parse import urlparse, parse_qs
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from HW9_PO.page import LoginPage, DownloadPage


def test_download_file(driver):
    # Данные для теста
    admin_url = 'http://127.0.0.1/admin'
    name = 'new'
    mask = 'test_mask'
    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, 'logo1.png')
    download_page = DownloadPage(driver)
    login_page = LoginPage(driver)
    # Авторизация
    driver.get(admin_url)
    login_page.login_on_page('admin', 'admin')
    WebDriverWait(driver, timeout=3).until(ec.title_contains('Dashboard'))
    # получить токен
    cur_url = driver.current_url
    parse_url = urlparse(cur_url)
    user_token = parse_qs(parse_url.query)['user_token'][0]
    # Переход на страницу загрузки и загрузка
    download_url = admin_url + '/index.php?route=catalog/download/add' + '&user_token=' + user_token
    driver.get(download_url)
    try:
        download_page.upload_file(download_url, filename, name, mask)
        WebDriverWait(driver, 3).until(ec.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        print("no alert")
    download_page.click_save_button()
    assert download_page.new_row_in_table(name)
    print('\nФайл ' + name + ' добавлен')




