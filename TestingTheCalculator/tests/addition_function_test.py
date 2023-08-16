import json
import random
import requests

from configuration import Configuration as conf


class TestAdditionFunctions:

    def test_addition_of_numbers(self) -> None:
        left = conf.integers()
        right = conf.integers()
        expected_result = left + right
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['result']
        if actual_result == expected_result:
            conf.response_function(left, right, expected_result, actual_result, dataset.text)
        else:
            conf.error_response_function(left, right, expected_result, actual_result, dataset.text)

    def test_addition_status_zero(self):
        left = conf.integers()
        right = conf.integers()
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == conf.zero:
            conf.response_status(conf.zero, actual_result, dataset.text)
        else:
            conf.error_response_status(conf.zero, actual_result, dataset.text)

    def test_left_addition_status_two(self):
        left = conf.integers()
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left}))
        actual_result = dataset.json()['statusCode']
        if actual_result == conf.two:
            conf.response_status(conf.two, actual_result, dataset.text)
        else:
            conf.error_response_status(conf.two, actual_result, dataset.text)

    def test_right_addition_status_two(self):
        right = conf.integers()
        dataset = requests.post(conf.url_addition, data=json.dumps({"y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == conf.two:
            conf.response_status(conf.two, actual_result, dataset.text)
        else:
            conf.error_response_status(conf.two, actual_result, dataset.text)

    def test_left_addition_status_three(self):
        left = conf.floating()
        right = conf.integers()
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == conf.three:
            conf.response_status(conf.three, actual_result, dataset.text)
        else:
            conf.error_response_status(conf.three, actual_result, dataset.text)

    def test_right_addition_status_three(self):
        left = conf.integers()
        right = conf.floating()
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == conf.three:
            conf.response_status(conf.three, actual_result, dataset.text)
        else:
            conf.error_response_status(conf.three, actual_result, dataset.text)

    def test_left_addition_status_four(self):
        left = conf.max_integers()
        right = conf.integers()
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == conf.four:
            conf.response_status(conf.four, actual_result, dataset.text)
        else:
            conf.error_response_status(conf.four, actual_result, dataset.text)

    def test_right_addition_status_four(self):
        left = conf.integers()
        right = conf.max_integers()
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == conf.four:
            conf.response_status(conf.four, actual_result, dataset.text)
        else:
            conf.error_response_status(conf.four, actual_result, dataset.text)

    def test_addition_status_five(self):
        left = conf.integers()
        right = conf.integers()
        dataset = requests.get(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == conf.five:
            conf.response_status(conf.five, actual_result, dataset.text)
        else:
            conf.error_response_status(conf.five, actual_result, dataset.text)

