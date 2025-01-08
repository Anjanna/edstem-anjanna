from sqlalchemy.dialects.postgresql import ENUM

from restaurant_api.app.config import db

price_range_enum = ENUM('LOW', 'MEDIUM', 'HIGH', name='price_range', create_type=True)
review_status_enum = ENUM('PENDING', 'APPROVED', name='review_status', create_type=True)

class Restaurant(db.Model):
    __tablename__ = "restaurant"
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    cuisine_type = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    price_range = db.Column(price_range_enum, nullable=False)
    average_rating = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    updated_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        """Returns a dict representation of the Restaurant model"""
        restaurant_dict = {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }
        restaurant_dict['created_date'] = str(restaurant_dict['created_date'])
        restaurant_dict['updated_date'] = str(restaurant_dict['updated_date'])
        return restaurant_dict


class Review(db.Model):
    __tablename__ = "review"
    id = db.Column(db.String(255), primary_key=True)
    restaurant_id = db.Column(db.String(255), db.ForeignKey('restaurant.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    visit_date = db.Column(db.Date, nullable=False)
    status = db.Column(review_status_enum, nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    updated_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        """Returns a dict representation of the Review model"""
        review_dict = {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }
        review_dict['created_date'] = str(review_dict['created_date'])
        review_dict['updated_date'] = str(review_dict['updated_date'])
        return review_dict


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    updated_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        """Returns a dict representation of the User model"""
        user_dict = {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }
        user_dict['created_date'] = str(user_dict['created_date'])
        user_dict['updated_date'] = str(user_dict['updated_date'])
        return user_dict
