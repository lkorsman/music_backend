from app.db.connection import get_connection

def top_artists(limit: int = 10):
   conn = get_connection()
   cursor = conn.cursor()

   cursor.execute(
      """
      SELECT a.id, a.name, SUM(s.play_count) AS total_plays
      FROM artists a 
      JOIN songs s ON s.artist_id = a.id
      GROUP BY a.id, a.name
      ORDER BY total_plays DESC
      LIMIT %s
      """,
      (limit,)
   )

   results = cursor.fetchall()

   cursor.close()
   conn.close()

   return results

def top_artists_for_user(user_id: int, limit: int = 10):
   conn = get_connection()
   cursor = conn.cursor()

   cursor.execute(
      """
      SELECT a.id, a.name, COUNT(p.id) AS total_plays
      FROM plays p 
      JOIN songs s ON p.song_id = s.id
      JOIN artists a ON s.artist_id = a.id
      WHERE p.user_id = %s
      GROUP BY a.id, a.name
      ORDER BY total_plays DESC
      LIMIT %s
      """,
      (user_id, limit)
   )

   results = cursor.fetchall()

   cursor.close()
   conn.close()

   return results

def artist_total_plays(artist_id: int):
   conn = get_connection()
   cursor = conn.cursor()

   cursor.execute(
      """
      SELECT SUM(s.play_count)
      FROM songs s 
      WHERE s.artist_id = %s
      """,
      (artist_id,)
   )

   total = cursor.fetchone()[0] or 0

   cursor.close()
   conn.close()

   return total