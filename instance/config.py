# /instance/config.py
import os

class Config(object):
    """
        Parent configuration class.
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """
        Configurations for Development.
    """
    DEBUG = True

class TestingConfig(Config):
    """
        Configuration for testing with separate test database.
    """
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True

class StagingConfig(Config):
    """
        Configuration for Staging.
    """
    DEBUG = True

class ProductionConfig(Config):
    """
        Configurations for Production
    """
    DEBUG = True
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
