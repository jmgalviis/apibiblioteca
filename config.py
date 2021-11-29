from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    pass


class DevelopmentConfig(Config):
    app_debug = os.environ['APP_DEBUG']
    connection = os.environ['DB_CONNECTION']
    db_host = os.environ['DB_HOST']
    db_database = os.environ['DB_DATABASE']
    db_username = os.environ['DB_USERNAME']
    db_password = os.environ['DB_PASSWORD']

    DEBUG = app_debug
    SQLALCHEMY_DATABASE_URI = f'{connection}://{db_username}:{db_password}@{db_host}/{db_database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_SQLALCHEMY_LOG_MESSAGES = False


config = {
    'development': DevelopmentConfig
}
