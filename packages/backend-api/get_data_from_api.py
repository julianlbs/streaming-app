"""
Helper module to make requests to a 3rd party api
"""

import unittest
import requests
from flask_socketio import emit
import json
import time

url_test = 'http://127.0.0.1:5000/get_dummy_data'


def get_data_from_api(url=url_test):
    """
    Get data from 3rd party api
    """
    return requests.get(url).content.decode()


def send_data(url=url_test):
    emit('data_point', get_data_from_api(url), broadcast=True)


class test_get_data_from_api(unittest.TestCase):
    def test_return(self, url=url_test):
        print(f"Test {url} - return {get_data_from_api(url)}")


def test_send_data():
    send_data(url=url_test)


# test_get_data_from_api().test_return()
# test_send_data()
