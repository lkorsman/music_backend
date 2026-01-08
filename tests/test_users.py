import uuid

def test_create_user(client):
   unique_username = f"test_user_{uuid.uuid4().hex[:6]}"
   response = client.post("/users", json={"username": unique_username})
   assert response.status_code == 200
   assert response.json()["username"] == unique_username