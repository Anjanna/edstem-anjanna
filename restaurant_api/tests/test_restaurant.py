import pytest

from restaurant_api import create_app
from restaurant_api.app.config import TestConfig, db
from restaurant_api.app.exceptions import ValidationException
from restaurant_api.app.services.restaurant import Restaurant
from restaurant_api.app.services.review import Review


@pytest.fixture(scope="session")
def app():
    app = create_app(TestConfig)

    # setup database
    with app.app_context():
        db.create_all()

    yield app

    # teardown database
    with app.app_context():
        db.drop_all()


def test_create_restaurant(app):
    with app.app_context():
        payload = {
            "name": "McDonalds",
            "cuisine_type": "Continental",
            "address": "America",
            "price_range": "MEDIUM"
        }
        response = Restaurant().create_restaurant(payload)
        db.session.commit()
        assert response['name'] == payload['name']


def test_get_restaurant(app):
    with app.app_context():
        response = Restaurant().get_restaurant(page_number=1, page_size=50)
        print(response)
        assert "restaurants" in response
        assert "total_records" in response
        assert response["total_records"] == 1


def test_create_review(app):
    with app.app_context():
        response = Restaurant().get_restaurant(page_number=1, page_size=50)
        restaurant_id = response['restaurants'][0]['id']
        payload = {
            "restaurant_id": restaurant_id,
            "rating": 3,
            "comment": "good",
            "visit_date": "01-11-2024"
        }
        response = Review().create_restaurant_review(payload)
        assert response['restaurant_id'] == payload['restaurant_id']
        assert response['status'] == 'APPROVED'


def test_get_restaurant_review(app):
    with app.app_context():
        response = Restaurant().get_restaurant(page_number=1, page_size=50)
        restaurant_id = response['restaurants'][0]['id']
        response = Review().get_restaurant_review(restaurant_id)
        assert "reviews" in response
        assert len(response['reviews']) == 1


def test_get_top_restaurants(app):
    with app.app_context():
        response = Restaurant().get_top_restaurants()
        assert 'restaurants' in response

def test_create_restaurant_negative():
    with pytest.raises(ValidationException):
        payload = {
            "name": "best food"
        }
        Restaurant().create_restaurant(payload)


def test_create_restaurant_review_negative():
    with pytest.raises(ValidationException):
        payload = {
            "rating": "1"
        }
        Review().create_restaurant_review(payload)
