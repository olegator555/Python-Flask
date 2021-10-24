import json

from flask import session, request


def decor(f):
    def wrapper(*args, **kwargs):
        print("Before")
        return f(*args, **kwargs)

    return wrapper


def group_validation():
    group_name = session.get('group_name', '')
    if group_name:
        return True
    return False


def group_validation_decorator(f):
    def wrapper(*args, **kwargs):
        if group_validation():
            return f(*args, **kwargs)
        return "Permission denied"

    return wrapper


target_app = "" if len(request.endpoint.split('.')) == 1 else request.endpoint.split('.')


def group_permission_validation():
    access_config = current_app.config['ACCESS_CONFIG']
    group_name = session.get('group_name', 'unauthorized')
    if group_name in access_config and target_app in access_config[group_name]:
        return True
    return False


def group_permission_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if group_permission_validation():
            return f(*args, **kwargs)
        return "Permission denied"

    return wrapper
