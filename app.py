from app import create_app

from config import config
from decouple import config as config_decouple


enviroment = config['development']

if config_decouple('PRODUCTION', default=False):
    enviroment = config['production']

app = create_app(enviroment)

if __name__ == '__main__':
    app.run()
