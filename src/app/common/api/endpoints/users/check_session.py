"""Create user API endpoint"""
from fastapi import status, Response
from src.app.common.api.endpoints.users.router import router
from .objects.session import Session
from .utils.check_session import check_session


@router.post('/check_session', status_code=status.HTTP_200_OK)
async def http_check_session(session: Session, response: Response):
    """Check session http method"""
    if not check_session(session):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {'status': 'Session not exists'}
    return {'status': 'Session exists'}
