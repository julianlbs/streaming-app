# """
# Backend API
# """

import flask
from get_batch_data import get_batch_data
from flask_socketio import SocketIO, emit
from get_data_from_api import get_data_from_api, send_data
import eventlet

eventlet.monkey_patch()

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")
# flask_cors.CORS(app, resources={r"/*": {"origins": "*"}})

dummy_data: list = []
api_service_url = 'http://127.0.0.1:5000/get_dummy_data'


# async def get_data_on_startup():
#     """Call get_batch_data when the server starts"""
#     global dummy_data
#     await get_batch_data(5000)
#     data = await get_batch_data(5000)
#     # dummy_data = data


# @app.route("/api")
# async def get_api_data():
#     """API that returns the list of 5000 dummy_data"""
#     if (len(dummy_data) == 0):
#         await get_data_on_startup()
#     return flask.jsonify({"data": dummy_data})


@socketio.on('stream_data')
def stream_data():
    for _ in range(5000):
        send_data()


# def emit_data():
#     for i in range(5):
#         socketio.emit('data_point', send_data())
#         eventlet.sleep(1)


@socketio.on("create")
def create_data():
    send_data()
    # threads = []
    # for _ in range(5):  # You can adjust the number of threads as needed
    #     thread = threading.Thread(target=emit_data)
    #     threads.append(thread)
    #     thread.start()

    # # Wait for all threads to complete
    # for thread in threads:
    #     thread.join()

    # proc = [multiprocessing.Process(target=send_data) for i in range(2)]

    # for p in proc:
    #     p.start()
    # for p in proc:
    #     p.join()

    # with multiprocessing.Pool() as pool:
    #     for result in pool.imap_unordered(send_data, iterable=[
    #             api_service_url for _ in range(2)], chunksize=1):
    #         print('finish')


# thread = threading.Thread(target=create_data)


if __name__ == '__main__':
    socketio.run(app, port=5001, debug=True,
                 use_reloader=True, log_output=True)
