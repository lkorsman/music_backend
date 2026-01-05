from pydantic import BaseModel

class SongCreate(BaseModel):
   id: int
   title: str
   artist: str
   duration: int

class SongOut(BaseModel):
   id: int
   title: str
   artist: str
   duration: int
   play_count: int
