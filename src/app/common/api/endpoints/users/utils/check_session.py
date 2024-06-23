"""Check if user exists"""
from src.app.common.api.endpoints.users.objects.session import Session
from src.app.utils.database import get_cursor
import datetime


def check_session(session: Session) -> bool:
    """Create user"""
    with get_cursor() as cursor:
        cursor.execute(
            '''
            SELECT * FROM user_sessions WHERE userid=%s AND session=%s
            ''',
            (session.userid, session.session_id)
        )
        session = cursor.fetchone()
    if not session:
        return False
    utcnow = datetime.datetime.utcnow()
    if session.expires_at < utcnow:
        return False
    return True
