from flask import Flask

from . import config, settings
from .settings import HOST, PORT, PROJECT
from .utils import make_celery


# Entire Flask application and its configuration.
app = Flask(__name__)
app.config.from_object(config.config[settings.CONFIG])
# Make custom celery object.
celery = make_celery(app)

# Exposing API capabilities and (de)serialization schemas.
from . import views
