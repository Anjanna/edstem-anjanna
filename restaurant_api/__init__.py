import json

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from restaurant_api.app.api.restaurant import restaurant_app
from restaurant_api.app.api.review import review_app
from restaurant_api.app.api.user import user_app
from restaurant_api.app.config import Config, db
from restaurant_api.app.exceptions import ValidationException
from restaurant_api.app.models.models import Restaurant, Review, User

migrate = Migrate()

def create_app(db_config=None):
    app = Flask(__name__)
    db_config = db_config if db_config else Config
    app.config.from_object(db_config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt = JWTManager(app)
    app.register_blueprint(restaurant_app)
    app.register_blueprint(review_app)
    app.register_blueprint(user_app)
    return app

app = create_app(Config)

@app.errorhandler(ValidationException)
def handle_validation_error(e):
    return json.dumps({'error': e.message}), e.status_code
