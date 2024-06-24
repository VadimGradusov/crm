"""Access levels"""
from src.app.utils.database import get_cursor


with get_cursor() as cursor:
    cursor.execute(
        '''
        SELECT * FROM access_levels
        '''
    )
    ACCESS_LEVELS = cursor.fetchall()
