from datetime import timedelta

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SECRET_KEY = "35b69b12458df628f040c2e0c200584fd603b67e03b95eb2f6ed18d1abf9f038"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@host.docker.internal:5432/restaurantdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = "35b69b12458df628f040c2e0c200584fd603b67e03b95eb2f6ed18d2jbj5h563"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


class TestConfig:
    SECRET_KEY = "35b69b12458df628f040c2e0c200584fd603b67e03b95eb2f6ed18d1abf9f038"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5432/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = "35b69b12458df628f040c2e0c200584fd603b67e03b95eb2f6ed18d2jbj5h563"