"""Handle /message page."""


from flask import (
    abort,
    request,
)

from pyproc import app, tasks
from pyproc.views.base import responsify


@app.route("/message", methods=["POST"])
@responsify
def message():
    """Messaging page available for users/clients submitting tasks."""
    # Retrieve JSON parameters data.
    data = request.get_json() or {}
    data.update(dict(request.values))
    msg = data.get("msg")
    if not msg:
        raise abort(400, "missing 'msg' data")

    # Deffer the message as a task.
    result = tasks.process_message.delay(msg, delta=10)
    task_id = result.task_id
    if not task_id or result.failed():
        raise abort(400, "task failed")
    # Then check and return ID.
    return {
        "task_id": result.id
    }


@app.route("/result", methods=["GET"])
@responsify
def result():
    """Get results when ready regarding a previously submitted task."""
    # Retrieve JSON parameters data.
    data = request.get_json() or {}
    data.update(dict(request.values))
    tid = data.get("tid")
    if not tid:
        raise abort(400, "missing 'tid' data")

    # Get the result (if exists and finished).
    result = tasks.process_message.AsyncResult(tid)
    # Return status and result if available.
    resp = {
        "status": result.status,
        "result": None,
    }
    if result.ready():
        resp["result"] = result.get()
    return resp
