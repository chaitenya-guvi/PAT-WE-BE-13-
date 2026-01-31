*** Settings ***
Library    BuiltIn

*** Variables ***
${MESSAGE}    Hello Robot

*** Test Cases ***
Print Message
    Log    ${MESSAGE}
    Custom Log    This is a custom log message
    Chaitenya custom keyword

*** Keywords ***
Custom Log
    [Arguments]    ${text}
    Log    ${text}

Chaitenya custom keyword
    Log to Console    This is a custom keyword by Chaitenya
