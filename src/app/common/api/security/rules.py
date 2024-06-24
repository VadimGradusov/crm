"""Check API access rules"""
from src.app.common.users.user import get_user
from src.app.common.users.objects.user import User
from src.configs.security import rules, roles, access_levels
from src.configs.common.users import UNAUTH_USER
from .sessions import get_userid_by_session, check_session_alive


def check_rules(endpoint: str, session_id: str, method: str) -> bool:
    """Check user rules"""
    userid = get_userid_by_session(session_id)
    user = get_user(userid)
    session_alive = check_session_alive(session_id)
    if not session_alive:
        user.roles = [UNAUTH_USER]
    endpoints = get_user_endpoints(user)
    return [endpoint, method] in endpoints


def get_user_endpoints(user: User) -> list:
    """Get user available endpoints"""
    endpoints = []
    for role in user.roles:
        endpoints += get_role_endpoints(role)
    return endpoints


def get_role_endpoints(role_id: int) -> list:
    """Get role endpoints"""
    return [[rule.endpoint, rule.method] for rule in rules.RULES if rule.role_id == role_id]


