import json

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from restaurant_api.app.services.restaurant import Restaurant
from restaurant_api.app.utils.utils import requires_role

restaurant_app = Blueprint("restaurant", __name__, url_prefix="/restaurant")

@jwt_required()
@requires_role(1)
def get_restaurant():
    restaurant = Restaurant()
    page_number = request.args.get('page_number', 1)
    page_size = request.args.get('page_size', 50)
    response = restaurant.get_restaurant(page_number, page_size)
    return json.dumps(response)

@jwt_required()
@requires_role(2)
def create_restaurant():
    payload = request.get_json()
    restaurant = Restaurant()
    response = restaurant.create_restaurant(payload)
    return json.dumps(response)

@jwt_required()
@requires_role(1)
def get_top_restaurants():
    restaurant = Restaurant()
    response = restaurant.get_top_restaurants()
    return json.dumps(response)


restaurant_app.add_url_rule(rule="", endpoint="get_restaurant", view_func=get_restaurant,
                     methods=["GET"])
restaurant_app.add_url_rule(rule="", endpoint="create_restaurant", view_func=create_restaurant,
                     methods=["POST"])
restaurant_app.add_url_rule(rule="/top", endpoint="get_top_restaurant", view_func=get_top_restaurants,
                     methods=["GET"])