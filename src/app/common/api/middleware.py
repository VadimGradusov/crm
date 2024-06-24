"""FastAPI Middleware"""
from fastapi import Request, Response, status
from src.app.core.fastapi.app import app
from .security.rules import check_rules


@app.middleware('http')
async def check_access(request: Request, call_next):
    """Access checker"""
    _json = await request.json()
    if not check_rules(request.url.path, _json['session_id'], request.method):
        return Response(content='Unauthorized', status_code=status.HTTP_401_UNAUTHORIZED)
    response = await call_next(request)
    return response
