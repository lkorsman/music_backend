from app.db.connection import get_connection
from app.models.artist import Artist
from sqlalchemy.orm import Session

def get_or_create_artist(db: Session, name: str) -> Artist:
   artist = db.query(Artist).filter(Artist.name == name).first()
   if not artist:
      artist = Artist(name=name)
      db.add(artist)
      db.commit()
      db.refresh(artist)
   return artist


def create_song(db: Session, song_data):
   artist_id = get_or_create_artist(db, song_data.artist_name)
   song = Song(
      title=song_data.title,
      artist_id=artist_id,
      duration=song_data.duration
   )

   db.add(song)
   db.commit()
   db.refresh(song)
   return song

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