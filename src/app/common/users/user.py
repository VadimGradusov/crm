"""User functions"""
from src.app.utils.database import get_cursor
from .objects.user import User
from src.configs.security.roles import ROLES
from src.configs.common.users import UNAUTH_USER, UNAUTH_GROUP


def get_user(userid: int):
    """Get user model by userid"""
    if userid == 0:
        return User(id=0, roles=[UNAUTH_USER], groups=[UNAUTH_GROUP])
    with get_cursor() as cursor:
        cursor.execute(
            '''
            SELECT u.id, u.username, ur.role_id, ug.group_id
            FROM users u 
            JOIN user_roles ur ON ur.userid=u.id 
            JOIN user_groups ug ON ug.userid=u.id
            WHERE u.id = %s
            ''',
            (userid, )
        )
        _user = cursor.fetchone()
    roles = get_parent_roles(_user.role_id, ROLES)
    return User(id=_user.id, username=_user.username,
                roles=[_user.role_id] + roles, groups=[_user.group_id])


def get_parent_roles(role_id, roles_dict):
    """Get parent roles"""
    roles_dict = {role.id: role for role in roles_dict}
    parent_roles = []
    current_role = roles_dict.get(role_id)
    while current_role and current_role.parent_id is not None:
        parent_role = roles_dict.get(current_role.parent_id)
        if parent_role:
            parent_roles.append(parent_role.id)
        current_role = parent_role
    return parent_roles
