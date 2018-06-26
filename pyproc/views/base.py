"""Base views, routes and utilities exposed by the pyproc web app."""


import functools

from flask import (
    jsonify
)


def responsify(func):
    """Decorator used to check authentication on views."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        resp = func(*args, **kwargs)
        return jsonify(resp)

    return wrapper
