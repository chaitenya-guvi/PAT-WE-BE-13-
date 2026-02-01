#https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-case-syntax
#https://robotframework.org/robotframework/latest/libraries/BuiltIn.html

# .robot  -
# .resource - Resource file to share keywords, variables, and settings across multiple test suites.
*** Settings ***
Resource  chaitenya.resource
Library  chaitenyaCustom.py

*** Test Cases ***

TC -01 String Length Verification
    [Documentation]    Verify the length of a given string
    generate random string of variable length
    generate random string chaitenya

