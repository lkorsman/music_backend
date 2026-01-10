from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.models.artist import Artist
from app.services.artist_analytics_service import (
   top_artists,
   top_artists_for_user,
   artist_total_plays
)
from app.schemas.artist import ArtistCreate, ArtistOut
from app.services.artist_service import (
   create_artist,
   get_artist_by_id
)
from app.db.database import get_db

router = APIRouter(prefix="/analytics/artists", tags=["artist analytics"])

@router.get("")
def list_artists(db: Session = Depends(get_db)):
    return db.query(Artist).all()

@router.post("", response_model=ArtistOut)
def create(artist: ArtistCreate, db: Session = Depends(get_db)):
   return create_artist(db, artist.name)

@router.get("/{artist_id}", response_model=ArtistOut)
def get_one(artist_id: int, db: Session = Depends(get_db)):
   artist = get_artist_by_id(db, artist_id)
   if not artist:
      raise HTTPException(status_code=404, detail="Artist not found")
   return artist

@router.get("/top")
def get_top_artists(limit: int = Query(10, le=100)):
   return top_artists(limit)

@router.get("/users/{user_id}/top")
def get_user_top_artists(user_id: int, limit: int = Query(10, le=100)):
   return top_artists_for_user(user_id, limit)

@router.get("/{artist_id}/plays/total")
def get_artist_total_plays(artist_id: int):
   return {"total_plays": artist_total_plays(artist_id)}