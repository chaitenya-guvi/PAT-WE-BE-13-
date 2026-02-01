*** Settings ***
#Library  SeleniumLibrary
Library    OperatingSystem


*** Variables ***
${URL}    https://www.example.com
${BROWSER}    Chrome

*** Test Cases ***
Open Browser and Verify Title
    [Documentation]    Open the browser, navigate to the URL, and verify the page title
    Remove Directory    yash