from flask import request
from functools import wraps
from flask_restful import abort

from itsdangerous import SignatureExpired, BadSignature

from users.models import User


def is_authenticated(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'is_authenticated', True):
            return func(*args, **kwargs)
        if 'Authorization' in request.headers:
            try:
                user = User.verify_auth_token(request.headers['Authorization'])
                return func(user, *args, **kwargs)
            except SignatureExpired:
                message = 'Token session expired.'
            except BadSignature:
                message = 'Invalid token passed.'
        return abort(403, **dict(detail=message))

    return wrapper
