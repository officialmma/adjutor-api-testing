def test_login_valid_user():
    """Test login with valid credentials"""
    
    payload = {
        "email": "dummyuser@example.com",
        "password": "DummyPass123"
    }

    response = requests.post(f"{BASE_URL}/login", json=payload)
    
    # Assert status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Assert the response message
    json_response = response.json()
    assert "token" in json_response, "Token not found in response"
    assert json_response["message"] == "Login successful", f"Unexpected message: {json_response['message']}"

def test_login_invalid_password():
    """Test login with incorrect password"""
    
    payload = {
        "email": "dummyuser@example.com",
        "password": "WrongPass123"
    }

    response = requests.post(f"{BASE_URL}/login", json=payload)
    
    # Assert status code
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    
    # Assert the response message
    json_response = response.json()
    assert json_response["message"] == "Invalid credentials", f"Unexpected message: {json_response['message']}"
