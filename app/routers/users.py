from fastapi import APIRouter
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import create_user

router = APIRouter(prefix="/users", tags=["users"]) # TODO look up what tags are

@router.post("/", response_model=UserOut)
def create(user: UserCreate):
    user_id = create_user(user.username)
    return {"id": user_id, "username": user.username}

@router.get("/")
def list_users():
    from app.db.connection import get_connection

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, username FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users