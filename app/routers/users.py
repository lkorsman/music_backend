from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.user import UserCreate, User
from app.services.user_service import create_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
def create(user: UserCreate):
    user_record = create_user(user.username)
    return JSONResponse(content=user_record)

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