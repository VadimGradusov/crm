"""Interacting with the Database"""
import mysql.connector
import contextlib
from src.configs.common.database import *


@contextlib.contextmanager
def get_cursor():
    """Open a connection to the database"""
    connection = mysql.connector.connect(user=DB_USERNAME,
                                         password=DB_PASSWORD,
                                         host=DB_HOST,
                                         database=DB_NAME)
    cursor = connection.cursor(buffered=True, named_tuple=True)
    try:
        yield cursor
    finally:
        connection.commit()
        connection.close()
