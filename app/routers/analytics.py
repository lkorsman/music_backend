from fastapi import APIRouter
from app.services.analytics_service import (
   top_songs,
   top_songs_for_user,
   total_plays_for_user,
)

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/top-songs")
def get_top_songs(limit: int = 10):
   return top_songs(limit)

@router.get("/users/{user_id}/top-songs")
def get_user_top_songs(user_id: int, limit: int = 10):
   return top_songs_for_user(user_id, limit)

@router.get("/users/{user_id}/total-plays")
def get_user_total_plays(user_id: int):
   return {"user_id": user_id, "total_plays": total_plays_for_user(user_id)}