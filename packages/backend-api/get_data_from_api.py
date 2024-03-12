import json
import aiohttp


async def get_data_from_api(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            return json.loads(data)
