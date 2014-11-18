from .database import db
from .simplemodel import SimpleModel


def init_db(app):
    db.init_app(app)


