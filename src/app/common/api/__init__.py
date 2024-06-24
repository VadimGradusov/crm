"""Init API"""
from src.app.core.fastapi.app import app
from src.app.common.api import middleware
from .endpoints import api


app.include_router(api,
                   prefix="/api/v1",
                   tags=["API_V1"])
