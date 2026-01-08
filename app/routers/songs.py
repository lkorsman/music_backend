from fastapi import APIRouter
from typing import List
from fastapi.responses import JSONResponse
from app.schemas.song import SongCreate, Song
from app.services.song_service import create_song, list_songs

router = APIRouter(prefix="/songs", tags=["songs"])

@router.post("/", response_model=Song)
def create(song: SongCreate):
   song_record = create_song(song)
   return JSONResponse(content=song_record)

@router.get("/", response_model=List[Song])
def list_all():
   return list_songs()