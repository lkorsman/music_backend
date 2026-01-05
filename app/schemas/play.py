from pydantic import BaseModel

class PlayCreate(BaseModel):
   user_id: int
   song_id: int