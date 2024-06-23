"""Check if user exists"""
from src.app.utils.database import get_cursor


def check_user_exists(username: str) -> bool:
    """Check if user exists"""
    with get_cursor() as cursor:
        cursor.execute(
            '''
            SELECT username FROM users WHERE username = %s
            ''',
            (username, )
        )
        username = cursor.fetchone()
    return bool(username)
