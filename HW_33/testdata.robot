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
    Get WebElement  xpath://*[contains(text(), 'Warning: Please check the form carefully for errors!')]
