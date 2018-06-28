#! /usr/bin/env bash

screen -dmS pyproc.worker celery -A pyproc.celery worker --loglevel=debug
screen -dmS pyproc.server gunicorn --reload -k eventlet -w 3 -b localhost:8080 --log-level debug --keep-alive 5 pyproc:app
