from fastapi import APIRouter
from app.services.artist_analytics_service import (
   top_artists,
   top_artists_for_user,
   artist_total_plays
)

router = APIRouter(prefix="/artists", tags=["artist analytics"])

@router.get("/top")
def get_top_artists(limit: int = 10):
   return top_artists(limit)

@router.get("/users/{user_id}/top")
def get_user_top_artists(user_id: int, limit: int = 10):
   return top_artists_for_user(user_id, limit)

@router.get("/{artist_id}/plays")
def get_artist_total_plays(artist_id: int):
   return {
      "artist_id": artist_id,
      "total_plays": artist_total_plays(artist_id)
   }