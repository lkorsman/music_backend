from app.db.connection import get_connection

def create_user(username: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username) VALUE (%s)",
        (username,)
    )
    conn.commit()

    user_id = cursor.lastrowid

    conn.close()

    return user_id