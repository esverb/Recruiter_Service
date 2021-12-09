import json


data = {
    "title" : "test title",
    "contact" : "@213414",
    "department" : "WBX",
    "description" : "Some description",
    "date_posted": "2022-08-21"}

def test_create_job(client):
    response = client.post("/job/create-job", json.dumps(data))
    assert response.status_code == 200


def test_retrieve_job_by_id(client):
    client.post("/job/create-job", json.dumps(data))
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "test title"