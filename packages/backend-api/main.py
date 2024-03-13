import asyncio
import concurrent.futures

import websockets
import json

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


async def handle_websocket(websocket, path):
    try:
        results = []

        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")

            REQUEST_STATE = 0

            if message == "stream_data":
                REQUEST_STATE += 1

                while (REQUEST_STATE < NUM_REQUESTS):
                    tasks = await gather_tasks(REQUEST_STATE, REQUEST_STATE + CHUNK_SIZE)

                    results = await asyncio.gather(*tasks)

                    sorted_results = await thread_sort_results(results)

                    await send_results(websocket, sorted_results)

                    REQUEST_STATE += CHUNK_SIZE

                await send_results(websocket, "close_connection")

    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed by the client.")


async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    start_server = websockets.serve(
        handle_websocket, "localhost", 8765)

    loop.run_until_complete(start_server)
    print("WebSocket server started")

    loop.run_forever()
