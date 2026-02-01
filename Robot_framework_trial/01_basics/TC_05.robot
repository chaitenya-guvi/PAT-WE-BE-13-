#https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-case-syntax
#https://robotframework.org/robotframework/latest/libraries/BuiltIn.html

# .robot  -
# .resource - Resource file to share keywords, variables, and settings across multiple test suites.

*** Settings ***
Library  String

*** Variables ***
${length}    5

*** Test Cases ***

TC -01 String Length Verification
    [Documentation]    Verify the length of a given string
    generate random string of variable length


*** Keywords ***
generate random string of variable length
    ${random_string}=  String.generate_random_string  ${length}
    Log To Console    Generated String: ${random_string}