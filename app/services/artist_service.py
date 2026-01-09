from sqlalchemy.orm import Session
from app.models.artist import Artist

def create_artist(db: Session, name: str) -> Artist:
   artist = Artist(name=name)
   db.add(artist)
   db.commit()
   db.refresh(artist)
   return artist

def get_artist_by_id(db: Session, artist_id: int):
   return db.query(Artist).filter(Artist.id == artist_id).first()

def list_artists(db: Session):
   return db.query(Artist).order_by(Artist.name).all()

def get_or_create_artist(db:Session, name: str):
   artist = db.query(Artist).filter(Artist.name == name).first()
   if artist:
      return artist

   artist = Artist(name=name)
   db.add(artist)
   db.commit()
   db.refresh(artist)

   return artist