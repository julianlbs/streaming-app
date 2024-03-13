from get_data_from_api import get_data_from_api
import asyncio
from flask_socketio import emit

api_service_url = 'http://127.0.0.1:5000/get_dummy_data'


async def get_batch_data(size: int):
    # dummy_data = []
    for i in range(size):
        emit('data_point', await get_data_from_api(api_service_url))
    # data = await asyncio.gather(*dummy_data)
    # return data
