import requests
import json

BASE_URL = "https://api.lendsqr.io/adjutor" 
def test_signup_valid_user():
    """Test signup with valid KYC and credentials"""
    payload = {
        "email": "dummyuser@example.com",
        "password": "DummyPass123",
        "kyc_info": {
            "first_name": "John",
            "last_name": "Doe",
            "date_of_birth": "1990-01-01",
            "address": "1234 Elm Street",
            "city": "Lagos",
            "country": "Nigeria",
            "id_type": "passport",
            "id_number": "A1234567",
            "issue_date": "2020-01-01",
            "expiry_date": "2030-01-01"
        }
    }

    response = requests.post(f"{BASE_URL}/signup", json=payload)
    
    # Assert status code
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    
    # Assert the response message
    json_response = response.json()
    assert "userId" in json_response, "UserId not found in response"
    assert json_response["message"] == "User registered successfully", f"Unexpected message: {json_response['message']}"

def test_signup_invalid_email():
    """Test signup with an invalid email format"""
    
    payload = {
        "email": "invalidemail",
        "password": "DummyPass123",
        "kyc_info": {
            "first_name": "John",
            "last_name": "Doe",
            "date_of_birth": "1990-01-01",
            "address": "1234 Elm Street",
            "city": "Lagos",
            "country": "Nigeria",
            "id_type": "passport",
            "id_number": "A1234567",
            "issue_date": "2020-01-01",
            "expiry_date": "2030-01-01"
        }
    }

    response = requests.post(f"{BASE_URL}/signup", json=payload)
    
    # Assert status code
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    
    # Assert the error message
    json_response = response.json()
    assert json_response["message"] == "Invalid email format", f"Unexpected message: {json_response['message']}"
