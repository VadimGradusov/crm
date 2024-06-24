"""Sessions"""
import datetime
from src.app.utils.database import get_cursor


def get_userid_by_session(session_id: str) -> int:
    """Returns userid by session id"""
    with get_cursor() as cursor:
        cursor.execute(
            '''
            SELECT userid FROM user_sessions WHERE session = %s
            ''',
            (session_id, )
        )
        session = cursor.fetchone()
    if not session:
        return 0
    return session.userid


def check_session_alive(session_id: str) -> bool:
    """Checking if session alive"""
    with get_cursor() as cursor:
        cursor.execute(
            '''
            SELECT expires_at FROM user_sessions WHERE session = %s
            ''',
            (session_id, )
        )
        session = cursor.fetchone()
    if not session:
        return False
    return datetime.datetime.utcnow() < session.expires_at
