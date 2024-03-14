import asyncio
from infra.get_data_from_api import get_data_from_api
import concurrent.futures
import json

API_URL = "http://127.0.0.1:5000/get_dummy_data"


class StreamHandler:
    REQUEST_STATE = 0

    def __init__(self, websocket, socket_data, CHUNK_SIZE, NUM_REQUESTS):
        self.websocket = websocket
        self.socket_data = socket_data
        self.CHUNK_SIZE = CHUNK_SIZE
        self.NUM_REQUESTS = NUM_REQUESTS

    async def handle(self):
        if self.socket_data["channel"] == "stream_data":
            filters = self.socket_data["filters"]
            self.REQUEST_STATE += 1

            results = []

            while (self.REQUEST_STATE < self.NUM_REQUESTS):
                tasks = await gather_tasks(self.REQUEST_STATE, self.REQUEST_STATE + self.CHUNK_SIZE)
                results = await asyncio.gather(*tasks)
                sorted_results = await thread_sort_results(results)
                filtered_results = filter_results(
                    sorted_results, ticker=filters["ticker"] if filters["ticker"] is not None else "")
                await send_results(self.websocket, filtered_results)


async def gather_tasks(start, end):
    return [get_data_from_api(API_URL, i)
            for i in range(start, end)]


async def thread_sort_results(results):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        ordered_results = list(executor.map(sort_result, results))

    sorted_results = [result for _, result in sorted(
        zip(ordered_results, results))]

    return sorted_results


def sort_result(item):
    return item['req_num']


def filter_results(results, ticker: str):
    filtered_results = []
    for result in results:
        if "data" in result and "ticker" in result["data"]:
            if ticker in result["data"]["ticker"]:
                filtered_results.append(result)
    return filtered_results


async def send_results(websocket, result):
    await websocket.send(json.dumps(result))
