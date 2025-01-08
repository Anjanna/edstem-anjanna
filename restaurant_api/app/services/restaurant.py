import datetime

from sqlalchemy import func

from restaurant_api.app.config import db
from restaurant_api.app.models.models import Restaurant as RestaurantModel
from restaurant_api.app.schemas.schema import RestaurantSchema
from restaurant_api.app.utils.utils import generate_uuid
from restaurant_api.app.utils.utils import validate_api_input_payload


class Restaurant:
    def __init__(self):
        self.now = datetime.datetime.now(datetime.timezone.utc)

    def create_restaurant(self,
                          payload: dict) -> dict:
        """
        This function adds the restaurant details into the database
        :param payload: contains details of the restaurant
        """
        validate_api_input_payload(payload, RestaurantSchema())
        restaurant = RestaurantModel(
            id = generate_uuid(),
            name = payload['name'],
            cuisine_type = payload['cuisine_type'],
            address = payload['address'],
            price_range = payload['price_range'],
            created_date = self.now,
            updated_date = self.now
        )
        db.session.add(restaurant)
        db.session.commit()
        return restaurant.to_dict()

    def get_restaurant(self,
                       page_number: int,
                       page_size: int) -> dict:
        """
        This function returns the details of the restaurant from the database
        :param payload: If present, contains the restaurant id 
        """
        total_records = db.session.query(RestaurantModel).count()
        pagination = RestaurantModel.query.paginate(page=page_number, per_page=page_size, error_out=False)
        result = pagination.items
        restaurants = [
            {
                "id": r.id,
                "name": r.name,
                "cuisine_type": r.cuisine_type,
                "address": r.address,
                "average_rating": r.average_rating if r.average_rating else "NA"
            }
            for r in result
        ]
        response = {"restaurants": restaurants, "total_records": total_records}
        return response

    def get_top_restaurants(self) -> dict:
        """
        This function returns the top 3 restaurants by cuisine type
        """
        restaurants = self.__get_top_3_restaurants_by_cuisine_query()
        data = [
            {
                "name": row.name,
                "cuisine_type": row.cuisine_type,
                "average_rating": row.average_rating,
            }
            for row in restaurants
        ]
        response = {"restaurants": data}
        return response

    def __get_top_3_restaurants_by_cuisine_query(self) -> list:
        """
        This function constructs the query to get top 3 restaurants by cuisine.
        """
        #Build a subquery that assigns a row number to each restaurant
        #within its cuisine group, sorted by average_rating desc.
        subq = (
            db.session.query(
                RestaurantModel.name,
                RestaurantModel.cuisine_type,
                RestaurantModel.average_rating,
                func.row_number()
                    .over(
                        partition_by=RestaurantModel.cuisine_type,
                        order_by=RestaurantModel.average_rating.desc()
                    )
                    .label("rn")
            )
            .subquery()
        )

        #Filter the subquery to get only rows where rn <= 3
        query = (
            db.session.query(subq)
            .filter(subq.c.rn <= 3)
            .order_by(subq.c.cuisine_type, subq.c.average_rating.desc())
        )

        #Execute and return the results
        return query.all()
