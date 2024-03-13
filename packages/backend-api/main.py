"""
Backend API
"""

import flask
from get_batch_data import get_batch_data
import flask_cors
from flask_socketio import SocketIO, emit

app = flask.Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
flask_cors.CORS(app, resources={r"/*": {"origins": "*"}})

dummy_data: list = []


async def get_data_on_startup():
    """Call get_batch_data when the server starts"""
    global dummy_data
    data = await get_batch_data(5000)
    dummy_data = data


@app.route("/api")
async def get_api_data():
    """API that returns the list of 5000 dummy_data"""
    if (len(dummy_data) == 0):
        await get_data_on_startup()
    return flask.jsonify({"data": dummy_data})


@socketio.on('stream_data')
def stream_data():
    emit('data_point', "hello")


if __name__ == '__main__':
    socketio.run(app, port=5001, debug=True,
                 use_reloader=True, log_output=True)
