"""Handle /message page."""


from flask import (
    abort,
)

from pyproc import app, settings, utils
from pyproc.views.base import responsify


@app.route("/message")
@responsify
def message():
    """Messaging page available for users/clients submitting tasks."""
    return {}
