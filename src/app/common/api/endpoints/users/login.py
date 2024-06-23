"""Login user"""
from fastapi import status, Response
from src.app.common.api.endpoints.users.router import router
from src.app.common.api.endpoints.users.utils.сheck_existence import check_user_exists
from src.app.common.api.endpoints.users.utils.login import check_password, register_session
from .objects.users import User


@router.post('/login', status_code=status.HTTP_200_OK)
async def http_login_method(user: User, response: Response):
    """http login method"""
    if not check_user_exists(user.username):
        response.status_code = status.HTTP_409_CONFLICT
        return {'status': 'User not exists'}
    if not check_password(user):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {'status': 'Invalid username or password'}
    session_id = register_session(user)
    return {'status': 'Session created', 'session_id': session_id}

