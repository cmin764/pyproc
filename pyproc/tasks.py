"""Here we define tasks processing logic with Celery."""


import time

from pyproc import celery


@celery.task()
def process_message(msg, delta=0):
    time.sleep(delta)
    msg = str(msg).capitalize()
    print(msg)
    return msg
