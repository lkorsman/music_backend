def test_create_song(client):
   response = client.post(
      "/songs",
      json={
         "title": "Test Song",
         "artist_name": "Test Artist",
         "duration": 100
      }
   )

   assert response.status_code == 200
   data = response.json()
   assert "id" in data
   assert data["title"] == "Test Song"
   assert data["artist"] == "Test Artist"
   assert data["play_count"] == 0
