# list variable and utilising for loop in robot

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}           https://www.saucedemo.com/
${BROWSER}       chrome
${USERNAME_FIELD}    id:user-name
${PASSWORD_FIELD}    id:password
${LOGIN_BUTTON}      id:login-button
${ERROR_MESSAGE}     xpath://h3[@data-test='error']
${PASSWORD}          secret_sauce

@{VALID_USERS}       standard_user    problem_user
@{LOCKED_USERS}      locked_out_user


*** Test Cases ***
Login With Valid Users
    FOR    ${user}    IN    @{VALID_USERS}
        Open SauceDemo
        Login To SauceDemo    ${user}    ${PASSWORD}
        Page Should Contain Element    id:inventory_container
        Close Browser
    END

Login With Locked Users
    FOR    ${user}    IN    @{LOCKED_USERS}
        Open SauceDemo
        Login To SauceDemo    ${user}    ${PASSWORD}
        Element Should Contain    ${ERROR_MESSAGE}    locked out
        Close Browser
    END


*** Keywords ***
Open SauceDemo
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login To SauceDemo
    [Arguments]    ${username}    ${password}
    Input Text    ${USERNAME_FIELD}    ${username}
    Input Text    ${PASSWORD_FIELD}    ${password}
    Click Button    ${LOGIN_BUTTON}
