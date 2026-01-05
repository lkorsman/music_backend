from app.db.connection import get_connection

def create_song(song):
   import time
   time.sleep(1)  # gives debugger time to attach
   conn = get_connection()
   cursor = conn.cursor(dictionary=True)

   cursor.execute(
      """
      INSERT INTO songs (id, title, artist, duration)
      VALUES (%s, %s, %s, %s)
      """,
      (song.id, song.title, song.artist, song.duration)
   )
   conn.commit()

   cursor.execute(
      """
      SELECT id, title, artist, duration, play_count 
      FROM songs
      WHERE id = %s
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
      "SELECT id, title, artist, duration, play_count FROM songs"
   )

   songs = cursor.fetchall()

   cursor.close()
   conn.close()

   return songs