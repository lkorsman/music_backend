from fastapi import APIRouter
from typing import List

from app.schemas.song import SongCreate, SongOut
from app.services.song_service import create_song, list_songs

router = APIRouter(prefix="/songs", tags=["songs"])

@router.post("/", response_model=SongOut)
def create(song: SongCreate):
   return create_song(song)

@router.get("/", response_model=List[SongOut])
def list_all():
   return list_songs()