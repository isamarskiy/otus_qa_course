*** Settings ***
Documentation    Suite description

Library  ./mylib.py

*** Variables ***
${NAME_ADMIN}  admin
${PASS_ADMIN}  admin
${EMAIL_MAIN}  test@ya.ru
${PASS_MAIN}   test


*** Test Cases ***
LoginAdmin
    Login Admin
    open page
    set username   ${NAME_ADMIN}
    set password   ${PASS_ADMIN}
    submit
    close

LoginMain
    Login Main
    open page
    set email   ${EMAIL_MAIN}
    set password   ${PASS_MAIN}
    submit
    close


