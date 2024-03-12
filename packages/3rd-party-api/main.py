"""Module with the api routes"""

import random
from datetime import datetime
import time
from flask import Flask, jsonify

app = Flask(__name__)

tickers = ["TICKER_1", "TICKER_2", "TICKER_3"]


@app.route("/get_dummy_data", methods=["GET"])
def get_dummy_data():
    """Get dummy data"""
    # Simulate a 1 second response time
    time.sleep(1)
    data = {
        "ticker": random.choice(tickers),
        "price": random.randint(1, 1000),
        "timestamp": datetime.now()
    }
    return jsonify(data)
