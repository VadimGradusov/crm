"""Users objects"""
from pydantic import BaseModel


class User(BaseModel):
    """User BaseModel class"""
    username: str
    password_hash: str
