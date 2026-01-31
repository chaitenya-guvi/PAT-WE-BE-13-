*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}    https://www.example.com
${BROWSER}    Chrome

*** Test Cases ***
Open Browser and Verify Title
    [Documentation]    Open the browser, navigate to the URL, and verify the page title
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Example Domain
    Close Browser