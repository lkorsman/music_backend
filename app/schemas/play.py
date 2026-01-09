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

   class Config:
      orm_mode = True