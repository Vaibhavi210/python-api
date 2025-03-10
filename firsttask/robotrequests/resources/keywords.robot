*** Settings ***
Suite Setup       Connect To Database    psycopg2    ${DBName}    ${DBUser}    ${DBPass}    ${DBHost}    ${DBPort}
Suite Teardown    Disconnect From Database
Library    RequestsLibrary
Library    DatabaseLibrary
Library    Process
Library    Collections
*** Variables ***
${BASE_URL}=    http://127.0.0.1:8000/
${DBHost}         localhost
${DBName}         student
${DBPass}         vaibhavi
${DBPort}         5432
${DBUser}         postgres
${forSubject}=    crudsubject/

*** Keywords ***
Register subject
        [Arguments]    ${subjectname} 
        Create Session    mysession    ${BASE_URL}  
        ${header}=    Create Dictionary    Content-Type=application/json
        ${data}=    Create Dictionary    subjectname=${subjectname}
        ${response}=    POST On Session    mysession     ${forSubject}   json=${data}    headers=${header}
        Log To Console   API Response Status Code: ${response.status_code}
        Log To Console  API Response Body: ${response.json()}  

        RETURN    ${response}


Register marks
        [Arguments]    ${subjectmarks}  ${subject_id}     ${student_id}
        Create Session    mysession    ${BASE_URL}  
        ${header}=    Create Dictionary    Content-Type=application/json
        ${data}=    Create Dictionary    subjectmarks=${subjectmarks}    subject_id=${subject_id}    student_id=${student_id}
        ${response}=    POST On Session    mysession     crudmarks/   json=${data}    headers=${header}
        Log To Console   API Response Status Code: ${response.status_code}
        Log To Console  API Response Body: ${response.json()}  

        RETURN    ${response}
Register student
        [Arguments]    ${name}    ${email}    ${profession}    ${subject_id}
        ${header}=    Create Dictionary     Content-Type=application/json
        ${subject_list}=    Create List    ${subject_id} 
        ${data}=    Create Dictionary     name=${name}    email=${email}   profession=${profession}    subject_id=${subject_list}
        Log To Console  Sending Data: ${data}
        ${response}=    POST      ${BASE_URL}/createuser/    json=${data}    headers=${header}
        Log To Console  API Response: ${response.json()}
        Should Be Equal As Strings    ${response.status_code}    200   User creation failed!
        RETURN     ${response}


Validate Student 
         [Arguments]    ${name}    ${email}    ${profession}    ${subject_id}
         Connect To Database     psycopg2    ${DBName}    ${DBUser}    ${DBPass}    ${DBHost}    ${DBPort}
         ${query_result}=    Query     SELECT * FROM helloapi_user WHERE email='${email}'
         Run Keyword If    ${query_result} == []    Fail    No student record found in the database.


         Log To Console   Query Result: ${query_result}
         ${db_id}    ${db_name}    ${db_email}    ${db_profession}=    Set Variable    ${query_result[0]}

         Should Not Be Empty    ${query_result}    Student registration failed, no data in the database.
         Should Be Equal As Strings    ${db_name}    ${name}
         Should Be Equal As Strings    ${db_email}    ${email}
         Should Be Equal As Strings    ${db_profession}    ${profession}
    
         Disconnect From Database

Fetch subject
        Create Session    mysession    ${BASE_URL}
        ${response}=     GET On Session  mysession   ${forSubject}/ 
        Log To Console    ${response}
        RETURN    ${response}

Fetch student
        [Arguments]    ${id}
        Create Session    mysession    ${BASE_URL}
        ${response}=    GET On Session     mysession    /getuser/${id}
        RETURN     ${response}

Fetch all students
        
        Create Session    mysession    ${BASE_URL}
        ${response}=    GET On Session     mysession    getalluser/
        RETURN     ${response}

Delete student
        [Arguments]    ${id}
        Create Session     mysession    ${BASE_URL}
        ${response}=    DELETE on Session    mysession    deleteuser/${id}
        RETURN    ${response}

Update student
        [Arguments]      ${id}  ${name}    ${email}    ${profession}    ${subject_id}
         ${header}=    Create Dictionary     Content-Type=application/json
        ${subject_list}=    Create List    ${subject_id} 
        ${data}=    Create Dictionary     name=${name}    email=${email}   profession=${profession}    subject_id=${subject_list}
        Log To Console  Sending Data: ${data}
        ${response}=    PUT      ${BASE_URL}updateusers/${id}/   json=${data}    headers=${header}
        Log To Console  API Response: ${response.json()}
        Should Be Equal As Strings    ${response.status_code}    200   User creation failed!
        RETURN     ${response}

