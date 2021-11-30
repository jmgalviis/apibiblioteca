from decouple import config


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='postgres::/localhost/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_SQLALCHEMY_LOG_MESSAGES = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='postgres::/localhost/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
