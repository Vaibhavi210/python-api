*** Settings ***
Library    RequestsLibrary
Library    DatabaseLibrary
Library    OperatingSystem
Resource    ../resources/keywords.robot
${

*** Test Cases ***

Register subject
        [Documentation]    Register a subject
        ${response}        Register subject     Hindi
        Should Be Equal As Strings  ${response.status_code}    200  
Register student
        [Documentation]    Register student and Validate
        ${response}    Register student    heer    heer@gmail.com    student      2
        Should Be Equal As Strings    ${response.status_code}    200
        Validate Student     heer    heer@gmail.com    student      2

Register marks
        [Documentation]    Register marks and Validate
        ${response}    Register marks    90    2     2
        Should Be Equal As Strings    ${response.status_code}    200
        


Duplicate Student
        [Documentation]    register the student again and check for the Duplicate
        ${response}    Register student    heer    heer@gmail.com    student      2
        Should Be Equal As Strings    ${response.status_code}    200
        ${error_list}=    Create List    user with this email already exists.


        ${expected_error}=    Create Dictionary    email=${error_list}


    
        Should Be Equal    ${response.json()}    ${expected_error}

Duplicate subject
        [Documentation]    register the subject again and check for the Duplicate
        ${response}    Register subject   Hindi
        Should Be Equal As Strings    ${response.status_code}    200
        ${error_list}=    Create List    subject with this subjectname already exists.


        ${expected_error}=    Create Dictionary    subjectname=${error_list}


    
        Should Be Equal    ${response.json()}    ${expected_error}
Fetch subject
    [Documentation]    fetch all subject
    ${response}    Fetch subject
    Should Be Equal As Strings    ${response.status_code}    200
    Log To Console    ${response.json()}

Fetch student
        [Documentation]     fetch single user
        ${response}    Fetch student    3
        Should Be Equal As Integers    ${response.status_code}    200
        Log To Console    ${response.json()}

Fetch all students
        [Documentation]     fetch all user
        ${response}    Fetch all students    
        Should Be Equal As Integers    ${response.status_code}    200
        Log To Console    ${response.json()}



Update student
        [Documentation]    update student and Validate
        ${response}    Update student    12    heer    heer@gmail.com    teacher      2
        Should Be Equal As Strings    ${response.status_code}    200
        Validate Student         heer    heer@gmail.com    teacher      2
Delete student
        [Documentation]    delete user by id 
        ${response}    Delete student    12
        Should Be Equal As Strings    ${response.status_code}    200
        Should Be Equal As Strings    ${response.json()}    user deleted successfully
        Log To Console    ${response.json()}

