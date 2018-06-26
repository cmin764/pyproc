"""Various general purpose utilities."""


import base64
import hashlib
import json
import os

import functools32

from pyproc import settings


def read(fpath):
    with open(os.path.join(settings.PROJECT, fpath)) as stream:
        return stream.read()


@functools32.lru_cache()
def get_secret_key():
    """Return a SHA256 hash as the default secret key."""
    # Obtain key bytes from default path.
    key_data = read(settings.SECRET_KEY_PATH)
    key = base64.b64decode(key_data)
    # Compute and return key hash.
    return hashlib.sha256(key).digest()


@functools32.lru_cache()
def get_broker():
    broker_data = read(settings.BROKER_CONN_PATH)
    broker_dict = json.loads(broker_data)
    return broker_dict
