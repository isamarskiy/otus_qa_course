from HW9_PO.page import LoginPage, DashboardPage, ProductEditPage


def test_add_picture(driver):
    driver.get('http://localhost/admin')
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    product_page = ProductEditPage(driver)
    im_name = ['logo1.png', 'logo2.png', 'logo3.jpg']

    login_page.login_on_page('admin', 'admin')
    dashboard_page.select_product_page()
    product_page.add_product('aaaTest_product', 'test', 'test')
    product_page.select_edit_product_by_name()
    product_page.select_tab_image()
    for name in im_name:
        product_page.add_im_button()
        product_page.click_on_image()
        product_page.click_on_edit_im()
        driver.find_element_by_xpath("//div[@id= 'modal-image']//img[@title= '%s']" % name).click()
    product_page.save_button()








