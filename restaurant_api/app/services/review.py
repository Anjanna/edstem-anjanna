import datetime
from sqlalchemy import func
from restaurant_api.app.config import db
from restaurant_api.app.models.models import Review as ReviewModel
from restaurant_api.app.models.models import Restaurant as RestaurantModel
from restaurant_api.app.utils.utils import generate_uuid
from restaurant_api.app.utils.utils import validate_api_input_payload
from restaurant_api.app.schemas.schema import ReviewSchema


class Review:
    def __init__(self):
        self.now = datetime.datetime.now(datetime.timezone.utc)

    def create_restaurant_review(self,
                                 payload: dict) -> dict:
        """
        This function adds a review about a restaurant to the database
        :param payload: contains details of the review
        """
        validate_api_input_payload(payload, ReviewSchema())
        review = ReviewModel(
            id = generate_uuid(),
            restaurant_id = payload['restaurant_id'],
            rating = payload['rating'],
            comment = payload['comment'],
            visit_date = datetime.datetime.strptime(payload['visit_date'], "%m-%d-%Y"),
            created_date = self.now,
            updated_date = self.now,
            status = "APPROVED"
        )
        db.session.add(review)
        rating_avg_query = db.session.query(func.avg(ReviewModel.rating)).filter(ReviewModel.restaurant_id == payload['restaurant_id'])
        average_rating = round(db.session.execute(rating_avg_query).scalar_one(), 2)
        RestaurantModel.query.filter_by(id=payload['restaurant_id']).update({"average_rating": average_rating})
        db.session.commit()
        return review.to_dict()

    def get_restaurant_review(self,
                              restaurant_id: str) -> dict:
        """
        This function returns the reviews of a restaurant from the database
        :param restaurant_id: contains the restaurant id 
        """
        #TODO payload validation
        data = ReviewModel.query.filter_by(restaurant_id=restaurant_id).all()
        res = [
            {
                "id": r.id,
                "rating": r.rating,
                "comment": r.comment,
            }
            for r in data
        ]
        response = {"reviews": res}
        return response
