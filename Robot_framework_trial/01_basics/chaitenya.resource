
*** Settings ***
Library  String
Resource    chaitenya.resource


*** Variables ***
${length}    5


*** Keywords ***
generate random string of variable length
    ${random_string}=  String.generate_random_string  ${length}
    Log To Console    Generated String: ${random_string}