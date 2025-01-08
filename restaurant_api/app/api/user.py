import json
from flask import request, Blueprint
from restaurant_api.app.services.user import User

user_app = Blueprint("user", __name__, url_prefix="/user")


def login():
    user = User()
    username = request.get_json()['name']
    response = user.login(username)
    return json.dumps(response)

def create_user():
    user = User()
    payload = request.get_json()
    response = user.create_user(payload)
    return response

user_app.add_url_rule(rule="/login", endpoint="login", view_func=login, methods=["POST"])
user_app.add_url_rule(rule="/create", endpoint="create_user", view_func=create_user, methods=["POST"])