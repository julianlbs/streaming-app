import asyncio
import websockets


class WebSocketServer:
    def __init__(self, websocket_handler):
        self.websocket_handler = websocket_handler

    def start_server(self):
        loop = asyncio.get_event_loop()
        start_server = websockets.serve(
            self.websocket_handler, "localhost", 8765)
        loop.run_until_complete(start_server)
        print("WebSocket server started")
        loop.run_forever()
