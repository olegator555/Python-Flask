from functools import wraps

from flask import session, request, current_app


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


def group_permission_validation(config: dict, sess:session) -> bool:
    group = session.get('group_name', 'unauthorized')
    target_app = "" if len(request.endpoint.split('.')) == 1 else request.endpoint.split('.')[1]
    print(target_app)
    if group in config and target_app in config[group]:
        return True
    return False


def group_permission_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if group_permission_validation(wrapper(), session):
            return f(*args, **kwargs)

        return "Permission denied"

    return wrapper
