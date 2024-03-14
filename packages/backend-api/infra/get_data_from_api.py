"""
Helper module to make requests to a 3rd party api
"""
import aiohttp


async def get_data_from_api(url, req_num):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=20) as response:
            api_data = await response.json()
            return {"data": api_data, "req_num": req_num}
