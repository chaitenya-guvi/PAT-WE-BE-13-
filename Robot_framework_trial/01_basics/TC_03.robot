*** Variables ***
${USER}    chaitenya

*** Test Cases ***
Conditional Login
    IF    '${USER}' == 'admin'
        Log To Console    Admin Login
    ELSE
        Log To Console   Normal Login
    END
