from app.db.connection import get_connection
from app.services.artist_service import get_or_create_artist

def create_song(song):
   artist_id = get_or_create_artist(song.artist_name)

   conn = get_connection()
   cursor = conn.cursor(dictionary=True)

   cursor.execute(
      """
      INSERT INTO songs (id, title, artist_id, duration)
      VALUES (%s, %s, %s, %s)
      """,
      (song.id, song.title, artist_id, song.duration)
   )
   conn.commit()

   cursor.execute(
      """
      SELECT s.id, s.title, a.name AS artist, s.duration, s.play_count 
      FROM songs s 
      JOIN artists a ON s.artist_id = a.id
      WHERE s.id = %s
      """,
      (song.id,)
   )
   created_song = cursor.fetchone()

   cursor.close()
   conn.close()

   return created_song

def list_songs():
   conn = get_connection()
   cursor = conn.cursor(dictionary=True)

   cursor.execute(
      """
      SELECT s.id, s.title, a.name AS artist, s.duration, s.play_count 
      FROM songs s 
      JOIN artists a ON s.artist_id = a.id
      """
   )

   songs = cursor.fetchall()

   cursor.close()
   conn.close()

   return songs