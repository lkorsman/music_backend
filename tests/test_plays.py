def test_play_song(client):
   response = client.post(
      "/plays",
      json={
         "user_id": 1,
         "song_id": 999
      }
   )

   assert response.status_code == 200
   assert response.json()["status"] == "played"