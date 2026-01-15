from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.artist import ArtistAnalyticsOut
from app.services.play_service import get_top_artists_for_user
from app.services.analytics_service import (
   top_songs,
   top_songs_for_user,
   total_plays_for_user,
)

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/songs/top")
def get_top_songs(limit: int = Query(10, le=100)):
   return top_songs(limit)

@router.get("/users/{user_id}/songs/top")
def get_user_top_songs(user_id: int, limit: int = Query(10, le=100)):
   return top_songs_for_user(user_id, limit)

@router.get("/users/{user_id}/plays/total")
def get_user_total_plays(user_id: int):
   return {"total_plays": total_plays_for_user(user_id)}

@router.get("/users/{user_id}/artists/top", response_model=List[ArtistAnalyticsOut])
def top_artists_for_user(user_id: int, limit: int = 10, db: Session = Depends(get_db)):
   try:
      return get_top_artists_for_user(db, user_id=user_id, limit=limit)
   except ValueError as e:
      raise HTTPException(status_code=404, detail=str(e))