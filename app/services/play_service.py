from app.db.connection import get_connection
from sqlalchemy.orm import Session
from app.models.play import Play
from app.models.song import Song
from app.models.user import User


def create_play(db: Session, user_id: int, song_id:int):
   play = Play(user_id=user_id, song_id=song_id)
   db.add(play)
   db.commit()
   db.refresh(play)
   return play

def list_plays(db: Session):
   return db.query(Play).all()

def record_play(db: Session, user_id: int, song_id:int) -> Play:
   song = db.query(Song).filter(Song.id == song_id).first()
   if not song:
      raise ValueError("Song not found")

   user = db.query(User).filter(User.id == user_id).first()
   if not user:
      raise ValueError("User not found")

   play = Play(user_id=user_id, song_id=song_id)
   db.add(play)

   song.play_count += 1

   db.commit()
   db.refresh(play)
   db.refresh(song)

   play.song_title = song.title
   play.artist_name = song.artist.name

   return play