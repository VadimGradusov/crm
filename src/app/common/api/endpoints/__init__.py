"""Init API endpoints"""
from fastapi import APIRouter
from src.app.common.api.endpoints.users import router as users


api = APIRouter()

api.include_router(users,
                   prefix="/users",
                   tags=["users"])
