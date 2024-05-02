import time
from celery import shared_task, states
from flask import current_app
from stapp.celstreamer.schema import StreamSchema


@shared_task(bind=True)
def stream_task(sch: StreamSchema):
    """Background task that runs a long function with progress reports."""
    print(sch)
    time.sleep(10)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}
