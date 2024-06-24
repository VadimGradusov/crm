"""Roles"""
from src.app.utils.database import get_cursor


with get_cursor() as cursor:
    cursor.execute(
        '''
        SELECT * FROM roles
        '''
    )
    ROLES = cursor.fetchall()
