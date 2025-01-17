from os import getenv
import logging
from flask.app import Flask
from flask_ask import Ask


if getenv('FLASK_ENV') == 'development':
    logging.getLogger('flask_ask').setLevel(logging.DEBUG)
    logging.getLogger(__name__).setLevel(logging.DEBUG)


route_prefix = getenv('ASKS_ROUTE_PREFIX', '/alexa')
tracks_count = int(getenv('ASKS_TRACKS_COUNT', 50))
locale = getenv('ASKS_LOCALE', 'en')

app = Flask(__name__)
ask = Ask(app, route_prefix, path='templates/%s.yaml' % locale)

logger = app.logger


from . import intents
