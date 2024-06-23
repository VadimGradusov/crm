"""Create user API endpoint"""
from fastapi import status, Response
from src.app.common.api.endpoints.users.router import router
from .objects.users import User
from .utils.сheck_existence import check_user_exists
from .utils.create import create_user


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def http_create_user(user: User, response: Response):
    """Create user http method"""
    if check_user_exists(user.username):
        response.status_code = status.HTTP_409_CONFLICT
        return {'status': 'User with this username already exists'}
    create_user(user)
    return {'status': 'User created'}
