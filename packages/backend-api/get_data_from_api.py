"""
Helper module to make requests to a 3rd party api
"""

import json
import aiohttp


async def get_data_from_api(url):
    """
    Get data from 3rd party api
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            return json.loads(data)
