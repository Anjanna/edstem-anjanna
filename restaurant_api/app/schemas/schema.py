from marshmallow import fields
from marshmallow import Schema


class RestaurantSchema(Schema):
    name = fields.Str(required=True)
    cuisine_type = fields.Str(required=True)
    address = fields.Str(required=True)
    price_range = fields.Str(required=True)


class ReviewSchema(Schema):
    restaurant_id = fields.Str(required=True)
    rating = fields.Integer(required=True)
    comment = fields.Str(required=True)
    visit_date = fields.Str(required=True)