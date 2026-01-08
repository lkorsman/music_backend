from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Song(Base):
   __tablename__ = "songs"
   id = Column(Integer, primary_key=True, index=True)
   title = Column(String(200), nullable=False)
   artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)
   duration = Column(Integer, nullable=False)
   play_count = Column(Integer, default=0)

   artist = relationship("Artist")