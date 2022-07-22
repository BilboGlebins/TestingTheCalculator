import requests
import unittest

from configuration import Configuration as conf


class TestStartFunctions(unittest.TestCase):

    def test_launch_status_zero(self):
        dataset = requests.get(conf.url_state)
        actual_result = dataset.json()['statusCode']
        if actual_result == conf.zero:
            conf.response_status(conf.zero, actual_result, dataset.text)
        else:
            conf.error_response_status(conf.zero, actual_result, dataset.text)

    def test_launch_status_five(self):
        dataset = requests.post(conf.url_state)
        actual_result = dataset.json()['statusCode']
        if actual_result == conf.five:
            conf.response_status(conf.five, actual_result, dataset.text)
        else:
            conf.error_response_status(conf.five, actual_result, dataset.text)


