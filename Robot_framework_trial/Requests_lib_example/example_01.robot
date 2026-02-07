*** Settings ***
Library               RequestsLibrary

*** Test Cases ***

Quick Get A JSON Body Test
    ${response}=    GET  https://jsonplaceholder.typicode.com/posts/1
    Should Be Equal As Strings    1  ${response.json()}[id]


Quick Get A JSON Body Test 2
    ${response}=    GET  https://jsonplaceholder.typicode.com/posts/1
    Status SHould Be


Quick Get A JSON Body Test 3
    ${response}=    GET  https://jsonplaceholder.typicode.com/posts/3000000
    Status SHould Be    404