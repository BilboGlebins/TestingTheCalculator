import json
import random
import requests
from configuration import Configuration as conf


class TestMultiplicationFunctions:

    def test_multiplication_of_numbers(self):
        left = random.randint(-2147483648, 2147483647)
        right = random.randint(-2147483648, left - 1)
        expected_result = left - right
        dataset = requests.post(conf.url_multiplication, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['result']
        if actual_result == expected_result:
            print()
            print(f"Left number: {left} | Right number: {right}")
            print(f"Expected result: {expected_result}")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print(f"Left number: {left} | Right number: {right}")
            print(f"Expected result: {expected_result}")
            print(f"Actual result: {actual_result}")