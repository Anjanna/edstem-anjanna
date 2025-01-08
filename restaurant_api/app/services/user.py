import datetime
from flask_jwt_extended import create_access_token
from restaurant_api.app.models.models import User as UserModel
from restaurant_api.app.utils.utils import generate_uuid
from restaurant_api.app.config import db


class User:
    def __init__(self):
        self.now = datetime.datetime.now(datetime.timezone.utc)

    def login(self,
              username: str) -> dict:
        """
        Logs in the user by returning a JWT access token
        """
        additional_claims = {"role": UserModel.query.filter_by(name=username).first().role}
        return {"access_token": create_access_token(identity=username, additional_claims=additional_claims)}

    def create_user(self,
                    payload: dict) -> dict:
        """
        Creates a user in the database
        :param payload: user details
        """
        user = UserModel(
            id = generate_uuid(),
            name = payload['name'],
            role = payload['role'],
            created_date = self.now,
            updated_date = self.now
        )
        db.session.add(user)
        db.session.commit()
        return user.to_dict()
