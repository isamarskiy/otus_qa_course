*** Settings ***
Documentation    Suite description

Library  SeleniumLibrary
Resource  testdata.robot
Test Teardown  Close all browsers


*** Test Cases ***
SuccessLogin
    OpenAdminPage
    Login

FailLogin
   OpenAdminPage
   FailLogin
   AssertFailtNotification


AddProduct
    OpenAdminPage
    Login
    Click Element  xpath://a[contains(text(),'Catalog')]
    Click Element  xpath://a[contains(text(),'Products')]
    sleep  5s
    Click Element  xpath://a[@data-original-title='Add New']
    Input text  name:product_description[6][name]   aaTest product
    Input text  name:product_description[6][meta_title]   Test tag1
    Click Element  partial link:Data
    Input text  name:model   Test model
    Click element  xpath://button[@data-original-title='Save']
    sleep  5s
    AssertSuccessNotification


EditProduct
    OpenAdminPage
    Login
    Click Element  xpath://a[contains(text(),'Catalog')]
    sleep  5s
    Click Element  xpath://a[contains(text(),'Products')]
    Click Element  xpath://td[contains(text(),'HP LP3065')]/parent::*//a
    Clear Element Text  name:product_description[1][name]
    Input text  name:product_description[1][name]  new_name
    Click Element  xpath://button[@data-original-title='Save']
    AssertSuccessNotification

DeleteProduct
    OpenAdminPage
    Login
    Click Element   xpath://a[contains(text(),'Catalog')]
    sleep  5s
    Click Element   xpath://a[contains(text(),'Products')]
    Select Checkbox  xpath://td[contains(text(),'Palm Treo Pro')]/parent::*//input
    Click Element   xpath://button[@data-original-title='Delete']
    Handle Alert
    AssertSuccessNotification









