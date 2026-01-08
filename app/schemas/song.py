from pydantic import BaseModel

class SongCreate(BaseModel):
   title: str
   artist_name: str
   duration: int

class Song(BaseModel):
   id: int
   title: str
   artist: str
   duration: int
   play_count: int
