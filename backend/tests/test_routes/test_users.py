import json


def test_create_user(client):
    data = {"username":"testusername", "email":"test@gmail.com", "password":"123456"}
    response = client.post("/register/", json.dumps(data))
    assert response.status_code == 200