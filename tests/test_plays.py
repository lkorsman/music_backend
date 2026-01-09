def test_play_song(client):
   response = client.post(
      "/plays",
      json={
         "user_id": 1,
         "song_id": 999
      }
   )

   assert response.status_code == 200
   data = response.json()
   assert data["user_id"] == 1
   assert data["song_id"] == 999

def test_list_plays(client):
   response = client.get("/plays")
   assert response.status_code == 200
   assert isinstance(response.json(), list)
