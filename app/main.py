from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.song import Song, SongCreate
from app.schemas.user import User, UserCreate
from app.services.song_service import create_song
from app.services.user_service import create_user
from dotenv import load_dotenv
from app.routers import users, songs, plays, analytics, artist_analytics
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="Music Streaming Backend")
app.include_router(users.router)
app.include_router(songs.router)
app.include_router(plays.router)
app.include_router(analytics.router)
app.include_router(artist_analytics.router)

@app.get("/")
def health_check():
    return {"status": "ok"}