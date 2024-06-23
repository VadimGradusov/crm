"""Check if user exists"""
from src.app.utils.database import get_cursor
from src.app.common.api.endpoints.users.objects.users import User


def create_user(user: User):
    """Create user"""
    with get_cursor() as cursor:
        cursor.execute(
            '''
            INSERT INTO users(username, password_hash) VALUES (%s, %s)
            ''',
            (user.username, user.password_hash)
        )
