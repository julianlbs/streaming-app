"""
Helper module to make requests to a 3rd party api
"""

import unittest
import requests


def get_data_from_api(url):
    """
    Get data from 3rd party api
    """
    return requests.get(url).content.decode()


class test_get_data_from_api(unittest.TestCase):
    def test_return(self, url='http://127.0.0.1:5000/get_dummy_data'):
        print(f"Test {url} - return {get_data_from_api(url)}")


test_get_data_from_api().test_return()
