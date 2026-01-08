from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Artist(Base):
   __tablename__ = "artists"

   id = Column(Integer, primary_key=True, index=True)
   name = Column(String(100), unique=True, nullable=False)