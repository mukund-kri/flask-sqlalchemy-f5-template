'''
Configuration using the inheritance patten given in the flask docs
'''
from os import pardir
from os.path import dirname, abspath, join


class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///develop.db'
    ROOT_DIR = abspath(dirname(__file__))


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/develop.db' % (Config.ROOT_DIR)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


from home import homebp

REGISTERED_BLUEPRINTS = [
    homebp
]
