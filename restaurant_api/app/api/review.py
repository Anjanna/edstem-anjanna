import json

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from restaurant_api.app.services.review import Review
from restaurant_api.app.utils.utils import requires_role

review_app = Blueprint("review", __name__, url_prefix="/review")

@jwt_required()
@requires_role(1)
def get_restaurant_review():
    review = Review()
    restaurant_id = request.args.get('restaurant_id')
    response = review.get_restaurant_review(restaurant_id)
    return json.dumps(response)

@jwt_required()
@requires_role(1)
def create_restaurant_review():
    review = Review()
    payload = request.get_json()
    response = review.create_restaurant_review(payload)
    return json.dumps(response)


review_app.add_url_rule(rule="", endpoint="get_restaurant_review", view_func=get_restaurant_review,
                     methods=["GET"])
review_app.add_url_rule(rule="", endpoint="create_restaurant", view_func=create_restaurant_review,
                     methods=["POST"])