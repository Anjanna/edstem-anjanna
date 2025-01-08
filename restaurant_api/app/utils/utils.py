import uuid
import json
from flask import request
from flask_jwt_extended import decode_token
from functools import wraps
from sqlalchemy import func
from restaurant_api.app.models.models import User as UserModel
from restaurant_api.app.exceptions import ValidationException

def generate_uuid():
    return uuid.uuid4().hex


def requires_role(required_role):
    """
    Decorator that restricts route access to users with at least the given role.
    For a simple single-role system, we check user.role == required_role.
    You can extend this logic for multiple roles or role hierarchies.
    """
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            jwt = request.headers.get('Authorization')
            if not jwt:
                return json.dumps({"error": "Unauthorized"})
            token = jwt.split(' ')[1]
            token = decode_token(token)
            user_role = token['role']
            # if user role is lower in the hierarchy, it is not enough to access the resource
            if user_role < required_role:
                return json.dumps({"error": "Forbidden"})
            
            return f(*args, **kwargs)
        return wrapped
    return decorator


def validate_api_input_payload(payload, schema):
    if errors := schema.validate(payload):
        raise ValidationException()
