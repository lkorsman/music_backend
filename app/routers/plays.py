from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.play import PlayOut
from app.services.play_service import create_play, list_plays, record_play

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