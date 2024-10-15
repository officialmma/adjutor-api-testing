def test_get_api_keys():
    """Test retrieving API keys after successful login"""
    
    # First, login and get the token
    login_payload = {
        "email": "dummyuser@example.com",
        "password": "DummyPass123"
    }
    
    login_response = requests.post(f"{BASE_URL}/login", json=login_payload)
    token = login_response.json()["token"]
    
    # Retrieve API keys with the token
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(f"{BASE_URL}/apikeys", headers=headers)
    
    # Assert status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Assert the response contains keys
    json_response = response.json()
    assert "apiKey" in json_response, "API key not found in response"
    assert json_response["message"] == "API keys retrieved successfully", f"Unexpected message: {json_response['message']}"
