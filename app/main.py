from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.routers import users, songs, plays, analytics

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)

app = FastAPI(title="Music Streaming Backend")
app.include_router(users.router)
app.include_router(songs.router)
app.include_router(plays.router)
app.include_router(analytics.router)

@app.get("/")
def health_check():
    return {"status": "ok"}