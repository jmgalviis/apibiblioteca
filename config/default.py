from decouple import config


DEBUG = True
SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='postgresql://postgres:postgres@localhost/apibiblioteca')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False
PROPAGATE_EXCEPTIONS = True
ERROR_404_HELP = False
