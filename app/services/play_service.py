from sqlalchemy.orm import Session
from sqlalchemy import func
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

def get_recent_plays_for_user(db: Session, user_id: int, limit: int = 10):
   user = db.query(User).filter(User.id == user_id).first()
   if not user:
      raise ValueError("User not found")

   recent_plays = (
      db.query(Play)
      .join(Play.song)
      .join(Song.artist)
      .filter(Play.user_id == user_id)
      .order_by(Play.played_at.desc())
      .limit(limit)
      .all()
   )

   for play in recent_plays:
      play.song_title = play.song.title
      play.artist_name = play.song.artist.name

   return recent_plays

def get_top_songs_for_user(db: Session, user_id: int, limit: int = 10):
   user = db.query(User).filter(User.id == user_id).first()
   if not user:
      raise ValueError("User not found")

   top_songs = (
      db.query(
         Song,
         func.count(Play.id).label("user_play_count")
      )
      .join(Play, Play.song_id == Song.id)
      .filter(Play.user_id == user_id)
      .group_by(Song.id)
      .order_by(func.count(Play.id).desc())
      .limit(limit)
      .all()
   )

   results = []
   for song, play_count in top_songs:
      play = Play(user_id=user_id, song_id=song.id)
      play.song_title = song.title
      play.artist_name = song.artist.name
      play.play_count = play_count
      results.append(play)

   return results