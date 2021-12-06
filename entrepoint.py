from decouple import config
from app import create_app

settings_module = config('APP_SETTINGS_MODULE')

app = create_app(settings_module)
