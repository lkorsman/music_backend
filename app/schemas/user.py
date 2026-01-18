from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str

class User(BaseModel):
    id: int
    username: str

class UserTopSongOut(BaseModel):
    song_id: int
    song_title: str
    artist_name: str
    play_count: int

    class Config:
        from_attributes = True
