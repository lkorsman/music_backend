from app.db.connection import get_connection

def get_or_create_artist(name: str) -> int:
   conn = get_connection()
   cursor = conn.cursor()

   cursor.execute(
      "SELECT id FROM artists WHERE name = %s",
      (name,)
   )

   row = cursor.fetchone()

   if row:
      artist_id = row[0]
   else:
      cursor.execute(
         "INSERT INTO artists (name) VALUE (%s)",
         (name,)
      )
      conn.commit()
      artist_id = cursor.lastrowid

   cursor.close()
   conn.close()

   return artist_id