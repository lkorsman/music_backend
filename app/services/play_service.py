from app.db.connection import get_connection
from sqlalchemy.orm import Session
from app.models.play import Play

def create_play(db: Session, user_id: int, song_id:int):
   play = Play(user_id=user_id, song_id=song_id)
   db.add(play)
   db.commit()
   db.refresh(play)
   return play

def list_plays(db: Session):
   return db.query(Play).all()

def record_play(user_id: int, song_id: int):
   conn = get_connection()
   cursor = conn.cursor()

   # Validate user exists
   cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
   if cursor.fetchone() is None:
      cursor.close()
      conn.close()
      raise ValueError("User not found")

   # Validate song exists
   cursor.execute("SELECT id FROM songs WHERE id = %s", (song_id,))
   if cursor.fetchone() is None:
      cursor.close()
      conn.close()
      raise ValueError("Song not found")

   # Insert play event
   cursor.execute(
      "INSERT INTO plays (user_id, song_id) VALUES (%s, %s)",
      (user_id,song_id)
   )

   # Increment play count
   cursor.execute(
      "UPDATE songs SET play_count = play_count + 1 WHERE id = %s",
      (song_id,)
   )

   conn.commit()
   cursor.close()
   conn.close()