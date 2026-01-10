from fastapi import APIRouter, Query
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