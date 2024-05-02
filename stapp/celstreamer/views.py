"""
Flask views

"""
from flask import Blueprint, current_app as app, jsonify, request
from pprint import pprint
from pydantic import ValidationError
from stapp.celstreamer.tasks import stream_task
from stapp.celstreamer.schema import StreamSchema

# # ============================================================================
# views
# ============================================================================

bp = Blueprint("streams", __name__, url_prefix="/streams")


@bp.route('/', methods=['GET'])
def index():
    """Index view"""
    pprint(app.config['RTMP_URI'])
    return jsonify({"data": "Hello World"}), 200


@bp.route('/entries', methods=['POST'])
def stream_control():
    """Index view"""

    json_data = request.get_json()
    pprint(json_data)
    try:
        control = StreamSchema(**json_data)
        pprint(control)

    except ValidationError as err:
        print(err)
        return jsonify({"messages": "data invalid"}), 422

    return jsonify({"data": "Healthy"}), 200


@bp.route('/health', methods=['GET'])
def health():
    """Index view"""

    return jsonify({"data": "Healthy"}), 200


# url = URI.parse("#{ENV['VIDEO_API_URL']}/streams/entries")
# data = { title: @video.title , stream_name: @video.stream_name, file_url: @video.url, stream_id: @video.id}

# @bp.route('/streams/entries', methods=['POST'])
# def longtask():
#     """
#     Route for starting long background task.
#
#     """
#     json_data = request.get_json()
#     pprint(json_data)
#     # task = long_task.apply_async()
#     req_schema = StreamSchema()
#     try:
#         req = req_schema.load(json_data)
#     except ValidationError as err:
#         return err.messages, 422
#
#     return jsonify({'Location': req}), 201

# route to modify the stream
#
#
# @app.route('/status/<task_id>')
# def taskstatus(task_id):
#     """Celery task status notifier."""
#     task = long_task.AsyncResult(task_id)
#     if task.state == 'PENDING':
#         # job has not started yet
#         response = {
#             'state': task.state,
#             'current': 0,
#             'total': 1,
#             'status': 'Pending..'
#         }
#     elif task.state != 'FAILURE':
#         response = {
#             'state': task.state,
#             'current': task.info.get('current', 0),
#             'total': task.info.get('total', 1),
#             'status': task.info.get('status', '')
#         }
#         if 'result' in task.info:
#             response['result'] = task.info['result']
#     else:
#         # something went wrong in the background job
#         response = {
#             'state': task.state,
#             'current': 1,
#             'total': 1,
#             'status': str(task.info),  # this's the exception raised
#         }
#
#     return jsonify(response)
# # ============================================================================
# EOF
# ============================================================================