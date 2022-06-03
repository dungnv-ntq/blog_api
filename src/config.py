import os


class Development(object):
    """
    Development environment configuration
    """

    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BUNDLE_ERRORS = True
    SQLALCHEMY_ECHO = True


class Production(object):
    """
    Production environment configuration
    """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BUNDLE_ERRORS = True


app_config = {
    'development': Development,
    'production': Production
}
