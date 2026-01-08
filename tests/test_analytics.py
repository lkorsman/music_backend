def test_top_songs(client):
   response = client.get("/analytics/top-songs")

   assert response.status_code == 200
   assert isinstance(response.json(), list)

def test_top_artists(client):
   response = client.get("/artists/top")

   assert response.status_code == 200
   assert isinstance(response.json(), list)