from fastapi import APIRouter, HTTPException
from app.schemas.play import PlayCreate
from app.services.play_service import record_play

router = APIRouter(prefix="/plays", tags=["plays"])

@router.post("/")
def play_song(play: PlayCreate):
   try:
      record_play(play.user_id, play.song_id)
      return {"status": "played"}
   except ValueError as e:
      raise HTTPException(status_code=404, detail=str(e))