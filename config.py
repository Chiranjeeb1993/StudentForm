import os

class Config(object):
    DEBUG = True
    SECRET_KEY = os.urandom(12)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///students.sqlite3"