"""Functions for login"""
import uuid
import datetime
from src.app.utils.database import get_cursor
from src.app.common.api.endpoints.users.objects.users import User
from src.configs.common.sessions import SESSION_ALIVE_HOURS


def check_password(user: User):
    """Check user password"""
    with get_cursor() as cursor:
        cursor.execute(
            '''
            SELECT * FROM users WHERE username = %s AND password_hash = %s
            ''',
            (user.username, user.password_hash)
        )
        user = cursor.fetchone()
    return bool(user)


def register_session(user: User):
    """Create user session"""
    with get_cursor() as cursor:
        cursor.execute(
            '''
            SELECT id FROM users WHERE username = %s AND password_hash = %s
            ''',
            (user.username, user.password_hash)
        )
        user = cursor.fetchone()
        utcnow = datetime.datetime.utcnow()
        expires_at = utcnow + datetime.timedelta(hours=SESSION_ALIVE_HOURS)
        session_id = str(uuid.uuid4())
        cursor.execute(
            '''
            INSERT INTO user_sessions(userid, session, expires_at)
            VALUES (%s, %s, %s)
            ''',
            (user.id, session_id, expires_at)
        )
    return session_id
