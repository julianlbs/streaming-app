import asyncio
import concurrent.futures

import websockets
import json
from main.create_websocket_server import WebSocketServer

from get_data_from_api import get_data_from_api

API_URL = "hhttp://127.0.0.1:5000/get_dummy_data"
NUM_REQUESTS = 5000
CHUNK_SIZE = 100


async def gather_tasks(start, end):
    return [get_data_from_api(API_URL, i)
            for i in range(start, end)]


def sort_result(item):
    return item['req_num']


async def thread_sort_results(results):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        ordered_results = list(executor.map(sort_result, results))

    sorted_results = [result for _, result in sorted(
        zip(ordered_results, results))]

    return sorted_results


async def send_results(websocket, result):
    await websocket.send(json.dumps(result))


def filter_results(results, ticker: str):
    filtered_results = []
    for result in results:
        if "data" in result and "ticker" in result["data"]:
            if ticker in result["data"]["ticker"]:
                filtered_results.append(result)
    return filtered_results


async def websocket_handler(websocket, path):
    try:
        results = []

        while True:
            socket_json = await websocket.recv()
            socket_data = json.loads(socket_json)
            print(f"Received message: {socket_data}")

            REQUEST_STATE = 0

            if socket_data["channel"] == "stream_data":
                filters = socket_data["filters"]
                REQUEST_STATE += 1

                while (REQUEST_STATE < NUM_REQUESTS):
                    tasks = await gather_tasks(REQUEST_STATE, REQUEST_STATE + CHUNK_SIZE)

                    results = await asyncio.gather(*tasks)

                    sorted_results = await thread_sort_results(results)
                    filtered_results = filter_results(
                        sorted_results, ticker=filters["ticker"] if filters["ticker"] is not None else "")
                    await send_results(websocket, filtered_results)

                    REQUEST_STATE += CHUNK_SIZE

                await send_results(websocket, "close_connection")

    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed by the client.")


async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

if __name__ == "__main__":
    ws_server = WebSocketServer(websocket_handler)
    ws_server.start_server()
