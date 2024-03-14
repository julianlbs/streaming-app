import websockets
import json
from main.stream_handler import StreamHandler

API_URL = "hhttp://127.0.0.1:5000/get_dummy_data"
NUM_REQUESTS = 5000
CHUNK_SIZE = 100


class WebSocketHandler:
    def __init__(self, websocket):
        self.websocket = websocket

    async def handle(self):
        try:
            while True:
                socket_json = await self.websocket.recv()
                socket_data = json.loads(socket_json)
                print(f"Received message: {socket_data}")
                await StreamHandler(self.websocket, socket_data,
                                    CHUNK_SIZE, NUM_REQUESTS).handle()
        except websockets.exceptions.ConnectionClosedOK:
            print("Connection closed by the client.")
