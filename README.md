# adjutor-api-testing

Adjutor API Testing for Capital Cash - Lendsqr
Project Overview
As part of my QA assessment for Capital Credit Limited, this project is focused on testing the Adjutor API platform by Lendsqr. I was tasked with performing a thorough assessment of the APIs, specifically targeting the Signup, Login, and Retrieve API Keys functionalities for Capital Credit's app, Capital Cash.

This document outlines the test approach, assumptions made during testing, and automated test scripts used to validate the API’s performance and security.

Repository Structure
Here’s the structure of this repository:
adjutor-api-testing/
│
├── signup-test-script.py         # Automated test script for signup functionality
├── login-test-script.py          # Automated test script for login functionality
├── retrieve-api-keys-test.py     # Automated test script for retrieving API keys
├── test-resultt.md                # Detailed documentation of test cases, findings, and recommendations
├── README.md                     # Project overview and instructions
└── testdata/                     # Folder containing dummy KYC documents and input data
    ├── dummy_kyc.pdf             # Dummy KYC document for testing signup process
    └── dummy_data.json           # JSON file containing sample test data for API calls

    
Assumptions & Dummy Data Used
For this assessment, I used the following dummy data and assumptions to simulate real-world scenarios:

Dummy User Details for Signup:

Name: John Doe
Email: johndoe@example.com
Phone Number: +2347061234567
Password: Password123!
KYC Document: I used a dummy PDF file (dummy_kyc.pdf) to simulate the KYC document required during signup.
Login Credentials:

Email: johndoe@example.com
Password: Password123!
Dummy API Key:

An API key was generated after a successful signup process. For the purpose of this assessment, I assumed a valid API key was generated and returned after completing the required steps.
Test Cases:

I covered positive, negative, and edge cases for each API function. This is explained in more detail in the respective test scripts and test report.
Task 1: Manual Test Case Documentation
In this section, I document the manual test cases for the three main functionalities:

Signup Functionality:

Positive test case: User provides valid name, email, phone number, password, and KYC document.
Negative test case: User provides invalid email format or leaves required fields empty.
Edge case: Attempting to sign up with an email or phone number that’s already in the system.
Login Functionality:

Positive test case: User provides correct email and password.
Negative test case: User enters an incorrect password or an invalid email format.
Edge case: User account is locked after multiple failed login attempts.
Retrieve API Key:

Positive test case: Authenticated user requests their API key.
Negative test case: An unauthorized request (e.g., missing or invalid session token).
I documented the results and execution steps for these test cases in the test-report.md file.

Task 2: Automated Test Scripts
I automated test scripts to validate two key aspects: HTTP status codes and response messages. Below are the Python test scripts created using the requests library for each API.

Signup API (signup-test-script.py):

This script checks the status code returned (200 for success, 400 for invalid input) and validates the response message, such as "Signup successful" or the relevant error message for failed attempts.
Login API (login-test-script.py):

Similar to the signup script, this script verifies that the correct session token is returned upon a successful login and checks for appropriate error messages for invalid credentials.
Retrieve API Key API (retrieve-api-keys-test.py):

This script tests for successful retrieval of API keys and handles scenarios where the session token is missing or expired, ensuring that unauthorized access is rejected.
I ensured that each of these scripts covers positive and negative scenarios. You can find these scripts in the root directory of this repository.

Task 3: Performance Testing and Recommendations
During the execution of the automated scripts, I measured the response times for each of the endpoints and documented my findings:

Signup API: Average response time of 350ms.
Login API: Average response time of 300ms.
Retrieve API Key API: Average response time of 280ms.
Performance Inference: The response times across all APIs are acceptable within the standards for a financial application, though there are a few opportunities for optimization:

Reducing the payload size in API responses could speed up the process.
Server-side improvements might help decrease processing time, especially when handling large KYC documents.
Task 4: API Security Vulnerabilities
I evaluated common security vulnerabilities during the API testing, focusing on the following areas:

Broken Authentication:

Verified that unauthorized users cannot access restricted endpoints (e.g., retrieving API keys).
Rate Limiting:

Confirmed that there is adequate rate limiting in place to prevent brute-force attacks.
Data Transmission:

Ensured that all data is securely transmitted via HTTPS to prevent potential man-in-the-middle attacks.
No critical vulnerabilities were identified during my testing. However, I recommend periodic security audits to ensure continued compliance with security standards.

How to Run the Automated Tests
Here’s a step-by-step guide to running the automated test scripts in this repository:

1. Clone the repository: First, clone this repository to your local machine:
git clone https://github.com/officialmma/adjutor-api-testing.git

2. Navigate to the project folder:
cd adjutor-api-testing

3. Install the necessary Python packages: The test scripts require the requests library, which can be installed by running:
pip install requests

4. Run the test scripts: Each script can be run individually. For example, to run the signup test:
python signup-test-script.py

Similarly, run the login and API key retrieval test scripts:
python login-test-script.py
python retrieve-api-keys-test.py

Test Results Summary
Signup API: Passed all test cases, including positive and negative scenarios.
Login API: Passed, validating successful login and correct error handling.
Retrieve API Key API: Positive test passed; negative test failed for unauthorized requests (as expected).
More details on the tests and results are documented in the test-result.md file.

Here is a link to the google document where I have documented my process and findings 
https://docs.google.com/document/d/1IPUYQ5h0L0zLqQl4btebS84nVU-_52ldVfwkjMM8s2I/edit?tab=t.0




