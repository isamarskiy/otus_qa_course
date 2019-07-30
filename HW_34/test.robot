*** Settings ***
Documentation    Suite description
Library  DatabaseLibrary
Library  SeleniumLibrary
Resource  testdata.robot
Library  SeleniumScreenshots

Test Teardown  Close all browsers

*** Test Cases ***
GetCountBeforeAdd
    ConnectToDB
    ${count} =   SelectFromDB
    should be true   ${count} == 12

AddProduct
    AddProduct

GetCountAfterAdd
    ConnectToDB
    ${count} =   SelectFromDB
    should be true   ${count} == 14

DeleteProduct
    DeleteProduct

GetCountAfterDelete
    ConnectToDB
    ${count} =   SelectFromDB
    should be true   ${count} == 13
