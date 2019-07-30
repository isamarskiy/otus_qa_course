*** Settings ***
Library  DatabaseLibrary

*** Variables ***
${DBPass}         ${EMPTY}
*** Keywords ***


OpenAdminPage
    Open Browser  http://127.0.0.1/admin/  Chrome
    Title Should be  Administration


InputUsername
    [Arguments]  ${user}
    Input Text   username  ${user}


InputPassword
    [Arguments]  ${password}
    Input Text    id:input-password  ${password}
    sleep  5s


Login
    InputUsername  admin
    InputPassword  admin
    sleep  1s
    Click Button  Login
    sleep  1s
    Title Should be  Dashboard


FailLogin
    InputUsername    admin
    InputPassword    admin1
    sleep  1s
    Click Button   Login
    sleep  1s

AssertFailtNotification
    Get WebElement  xpath://*[contains(text(), 'No match for Username and/or Password')]

AssertSuccessNotification
    Get WebElement  xpath://*[contains(text(), 'Success: You have modified products!')]


ConnectToDB
    Connect To Database  pymysql  bitnami_opencart  bn_opencart  ${DBPass}  127.0.0.1   4407

AddProduct
    OpenAdminPage
    Login
    Click Element  xpath://a[contains(text(),'Catalog')]
    Click Element  xpath://a[contains(text(),'Products')]
    sleep  5s
    Click Element  xpath://a[@data-original-title='Add New']
    Input text  name:product_description[1][name]   Asus
    Input text  name:product_description[1][meta_title]   Test asus
    Click Element  partial link:Data
    Input text  name:model   Test asus
    Click element  xpath://button[@data-original-title='Save']
    sleep  5s
    AssertSuccessNotification

DeleteProduct
    OpenAdminPage
    Login
    Click Element   xpath://a[contains(text(),'Catalog')]
    sleep  5s
    Click Element   xpath://a[contains(text(),'Products')]
    Select Checkbox  xpath://td[contains(text(),'Asus')]/parent::*//input
    Click Element   xpath://button[@data-original-title='Delete']
    Handle Alert
    AssertSuccessNotification

SelectFromDB
    ${query} =  Query  select count(*) from oc_product;
    [return]  ${query[0][0]}