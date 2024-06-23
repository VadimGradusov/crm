"""Session objects"""
from pydantic import BaseModel


class Session(BaseModel):
    """Session BaseModel class"""
    userid: int
    session_id: str
