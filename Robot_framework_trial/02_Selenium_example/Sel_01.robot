# Documentation: This Robot Framework test suite demonstrates basic login functionality testing for the SauceDemo website using SeleniumLibrary.
# [Arguments] - this section in a keyword defines the parameters that the keyword accepts.

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}           https://www.saucedemo.com/
${BROWSER}       chrome
${USERNAME_FIELD}    id:user-name
${PASSWORD_FIELD}    id:password
${LOGIN_BUTTON}      id:login-button
${ERROR_MESSAGE}     xpath://h3[@data-test='error']

${STANDARD_USER}      standard_user
${LOCKED_USER}        locked_out_user
${PROBLEM_USER}       problem_user
${PASSWORD}           secret_sauce


*** Test Cases ***
Login With Standard User
    Open SauceDemo
    Login To SauceDemo    ${STANDARD_USER}    ${PASSWORD}
    Page Should Contain Element    id:inventory_container
    Close Browser

Login With Locked Out User
    Open SauceDemo
    Login To SauceDemo    ${LOCKED_USER}    ${PASSWORD}
    Element Should Contain    ${ERROR_MESSAGE}    locked out
    Close Browser

Login With Problem User
    Open SauceDemo
    Login To SauceDemo    ${PROBLEM_USER}    ${PASSWORD}
    Page Should Contain Element    id:inventory_container
    Close Browser


*** Keywords ***
Open SauceDemo
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login To SauceDemo
    [Documentation]    Logs into the SauceDemo application with given username and password
    [Arguments]    ${username}    ${password}
    Input Text    ${USERNAME_FIELD}    ${username}
    Input Text    ${PASSWORD_FIELD}    ${password}
    Click Button    ${LOGIN_BUTTON}
