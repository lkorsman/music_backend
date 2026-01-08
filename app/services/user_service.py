from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, username:str):
    user = User(username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user