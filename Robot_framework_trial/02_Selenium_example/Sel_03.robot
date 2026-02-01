*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}               https://www.saucedemo.com/
${BROWSER}           chrome
${USERNAME_FIELD}    id:user-name
${PASSWORD_FIELD}    id:password
${LOGIN_BUTTON}      id:login-button
${ERROR_MESSAGE}     xpath://h3[@data-test='error']
${PASSWORD}          secret_sauce

&{USERS}
...    standard_user=valid
...    problem_user=valid
...    locked_out_user=locked


*** Test Cases ***
Login Validation For All Users
    FOR    ${username}    ${expected}    IN    &{USERS}
        Open SauceDemo
        Login To SauceDemo    ${username}    ${PASSWORD}
        Validate Login Result    ${expected}
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

Validate Login Result
    [Arguments]    ${expected}

    IF    '${expected}' == 'valid'
        Page Should Contain Element    id:inventory_container
    ELSE IF    '${expected}' == 'locked'
        Element Should Contain    ${ERROR_MESSAGE}    locked out
    END
