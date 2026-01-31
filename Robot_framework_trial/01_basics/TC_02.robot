*** Settings ***
Library    BuiltIn

*** Variables ***
${MESSAGE}    Hello Robot

*** Test Cases ***
Print Message
    Log    ${MESSAGE}

*** Keywords ***
Custom Log
    [Arguments]    ${text}
    Log    ${text}
