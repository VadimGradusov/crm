"""User model"""
from typing import List
from pydantic import BaseModel


class User(BaseModel):
    """User model"""
    id: int
    username: str = None
    roles: List[int]
    groups: List[int]
