"""Default settings for pyproc."""


import os


# Server settings.
HOST = "0.0.0.0"
PORT = 8080
DEBUG = True
CONFIG = os.getenv("FLASK_CONFIG") or "default"

# Authentication related settings.
ETC = os.path.join("etc", "pyproc")
SECRET_KEY_PATH, BROKER_CONN_PATH = map(
    lambda name: os.path.join(ETC, name),
    [
        "secret.key",
        "broker.json",
    ]
)

# Miscellaneous.
TEMPLATE_ENCODING = "utf-8"
PROJECT = os.path.normpath(
    # Project directory (package parent).
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir
    )
)
