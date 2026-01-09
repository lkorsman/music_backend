from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.play import PlayCreate, PlayOut
from app.services.play_service import create_play, list_plays

router = APIRouter(prefix="/plays", tags=["plays"])

@router.post("", response_model=PlayOut)
def create(play: PlayCreate, db: Session = Depends(get_db)):
   return create_play(db, play.user_id, play.song_id)

@router.get("", response_model=List[PlayOut])
def list_all(db: Session = Depends(get_db)):
   return list_plays(db)