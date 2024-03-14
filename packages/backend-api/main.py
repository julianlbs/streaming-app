from main.create_websocket_server import WebSocketServer
from main.websocket_handler import WebSocketHandler


async def websocket_handler(websocket):
    await WebSocketHandler(websocket).handle()

if __name__ == "__main__":
    ws_server = WebSocketServer(websocket_handler)
    ws_server.start_server()
