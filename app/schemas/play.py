from pydantic import BaseModel
from datetime import datetime

class PlayCreate(BaseModel):
   user_id: int
   song_id: int

class PlayOut(BaseModel):
   id: int
   user_id: int
   song_id: int
   played_at: datetime
   song_title: str
   artist_name: str

   class Config:
      from_attributes = True