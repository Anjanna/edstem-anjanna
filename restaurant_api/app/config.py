import os
from datetime import timedelta

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SECRET_KEY = "35b69b12458df628f040c2e0c200584fd603b67e03b95eb2f6ed18d1abf9f038"
    SQLALCHEMY_DATABASE_URI = os.environ['POSTGRES_DEV_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = os.environ['JWT_DEV_SECRET']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


class TestConfig:
    SECRET_KEY = "35b69b12458df628f040c2e0c200584fd603b67e03b95eb2f6ed18d1abf9f038"
    SQLALCHEMY_DATABASE_URI = os.environ['POSTGRES_TEST_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = os.environ['JWT_DEV_SECRET']