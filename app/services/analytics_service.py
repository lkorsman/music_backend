from app.db.connection import get_connection

def top_songs(limit: int = 10):
   conn = get_connection()
   cursor = conn.cursor(dictionary=True)

   cursor.execute(
      """
      SELECT
         s.id,
         s.title,
         a.name AS artist,
         s.play_count
      FROM songs s 
      JOIN artists a ON s.artist_id = a.id
      ORDER BY s.play_count DESC
      LIMIT %s
      """,
      (limit,)
   )

   results = cursor.fetchall()

   cursor.close()
   conn.close()

   return results

def top_songs_for_user(user_id: int, limit: int = 10):
   conn = get_connection()
   cursor = conn.cursor(dictionary=True)

   cursor.execute(
      """
      SELECT s.id, s.title, s.artist, COUNT(p.id) AS play_count
      FROM plays p 
      JOIN songs s ON p.song_id = s.id
      WHERE p.user_id = %s
      GROUP BY s.id, s.title, s.artist
      ORDER BY play_count DESC
      LIMIT %s
      """,
      (user_id, limit)
   )

   results = cursor.fetchall()

   cursor.close()
   conn.close()

   return results

def total_plays_for_user(user_id: int):
   conn = get_connection()
   cursor = conn.cursor()

   cursor.execute(
      "SELECT COUNT(*) FROM plays WHERE user_id = %s",
      (user_id,)
   )

   count = cursor.fetchone()[0]

   cursor.close()
   conn.close()

   return count