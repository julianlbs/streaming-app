"""
Backend API
"""

import flask
from get_batch_data import get_batch_data
import flask_cors
from flask_socketio import SocketIO, emit
from get_data_from_api import get_data_from_api
import asyncio
import time
import json
from get_data_from_api import get_data_from_api
import threading
import concurrent.futures

app = flask.Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
flask_cors.CORS(app, resources={r"/*": {"origins": "*"}})

dummy_data: list = []
api_service_url = 'http://127.0.0.1:5000/get_dummy_data'


async def get_data_on_startup():
    """Call get_batch_data when the server starts"""
    global dummy_data
    await get_batch_data(5000)
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


@socketio.on("create")
def create_data():
    data = get_data_from_api('http://127.0.0.1:5000/get_dummy_data')

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        thread.start()
        task_results = [executor.submit(data, i) for i in range(1000)]


thread = threading.Thread(target=create_data)


if __name__ == '__main__':
    socketio.run(app, port=5001, debug=True,
                 use_reloader=True, log_output=True)
