"""Backend API"""

import asyncio
from flask import Flask, jsonify
from get_data_from_api import get_data_from_api
app = Flask(__name__)


api_service_url = 'http://127.0.0.1:5000/get_dummy_data'


@app.route("/api", methods=["GET"])
async def steam_data():
    """API that returns the list of 5000 dummy_data"""
    dummy_data = []
    for i in range(5000):
        dummy_data.append(get_data_from_api(api_service_url))
    data = await asyncio.gather(*dummy_data)
    return jsonify({
        "data": data
    })

if __name__ == '__main__':
    app.run(port=5001)
