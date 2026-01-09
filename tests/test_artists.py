def test_create_artist(client):
   response = client.post(
      "/artists",
      json={"name": "Gang Starr"}
   )

   assert response.status_code == 200
   assert response.json()["name"] == "Gang Starr"

def test_list_artists(client):
   response = client.get("/artists")
   assert response.status_code == 200
   assert isinstance(response.json(), list)

def test_get_artist_by_id(client):
   create = client.post("/artists", json={"name": "Slayer"})
   artist_id = create.json()["id"]

   response = client.get(f"/artists/{artist_id}")
   assert response.status_code == 200
   assert response.json()["name"] == "Slayer"