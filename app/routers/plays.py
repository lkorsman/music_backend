from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.play import PlayOut
from app.services.play_service import list_plays, record_play, get_recent_plays_for_user, get_top_songs_for_user

router = APIRouter(prefix="/plays", tags=["plays"])

@router.get("", response_model=List[PlayOut])
def list_all(db: Session = Depends(get_db)):
   return list_plays(db)

@router.post("/{song_id}", response_model=PlayOut)
def play_song(song_id: int, user_id: int, db: Session = Depends(get_db)):
   try:
      play = record_play(db, user_id=user_id, song_id=song_id)
      return play
   except ValueError as e:
      raise HTTPException(status_code=404, detail=str(e))

@router.get("/recent/{user_id}", response_model=List[PlayOut])
def recent_plays(user_id: int, limit: int = 10, db: Session = Depends(get_db)):
   try:
      plays = get_recent_plays_for_user(db, user_id=user_id, limit=limit)
      return plays
   except ValueError as e:
      raise HTTPException(status_code=404, detail=str(e))

@router.get("/top/{user_id}", response_model=List[PlayOut])
def top_songs(user_id: int, limit: int = 10, db: Session = Depends(get_db)):
   try:
      return get_top_songs_for_user(db, user_id=user_id, limit=limit)
   except ValueError as e:
      raise HTTPException(status_code=404, detail=str(e))