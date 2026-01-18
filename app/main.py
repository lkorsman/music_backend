from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routers import(
    users,
    songs,
    plays,
    analytics,
    artist_analytics,
)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)

router = APIRouter()

app = FastAPI(title="Music Streaming Backend")
app.include_router(users.router)
app.include_router(songs.router)
app.include_router(plays.router)
app.include_router(analytics.router)
app.include_router(artist_analytics.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "ok"}