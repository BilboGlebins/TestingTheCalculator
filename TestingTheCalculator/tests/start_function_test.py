import json

import requests
import random
from configuration import Configuration as conf


class TestStartFunctions:

    def test_launch_status_zero(self):
        dataset = requests.get(conf.url_state)
        actual_result = dataset.json()['statusCode']
        if actual_result == 0:
            print()
            print("Expected result: 0")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 0")
            print(f"Actual result: {actual_result}")

    def test_launch_status_five(self):
        dataset = requests.post(conf.url_state)
        actual_result = dataset.json()['statusCode']
        if actual_result == 5:
            print()
            print("Expected result: 5")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 5")
            print(f"Actual result: {actual_result}")

    def test_addition_status_zero(self):
        left = random.randint(-2147483648, 2147483647)
        right = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 0:
            print()
            print("Expected result: 0")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 0")
            print(f"Actual result: {actual_result}")

    def test_addition_status_two(self):
        left = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 2:
            print()
            print("Expected result: 2")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 2")
            print(f"Actual result: {actual_result}")

    def test_addition_status_three(self):
        left = random.uniform(-2147483648, 2147483647)
        right = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 3:
            print()
            print("Expected result: 3")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 3")
            print(f"Actual result: {actual_result}")

    def test_addition_status_four(self):
        left = random.randint(2147483647+3, 3000000000)
        right = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 4:
            print()
            print("Expected result: 4")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 4")
            print(f"Actual result: {actual_result}")

    def test_addition_status_five(self):
        left = random.uniform(-2147483648, 2147483647)
        right = random.uniform(-2147483648, 21474836)
        dataset = requests.get(conf.url_addition, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 5:
            print()
            print("Expected result: 5")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 5")
            print(f"Actual result: {actual_result}")

    def test_multiplication_status_zero(self):
        left = random.randint(-2147483648, 2147483647)
        right = random.randint(-2147483648, left - 1)
        dataset = requests.post(conf.url_multiplication, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 0:
            print()
            print(f"Expected result: 0")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print(f"Expected result: 0")
            print(f"Actual result: {actual_result}")

    def test_multiplication_status_one(self):
        left = random.randint(-2147483648, 2147483647)
        right = random.randint(left+1, 2147483647)
        dataset = requests.post(conf.url_multiplication, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 1:
            print()
            print(f"Expected result: 1")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print(f"Expected result: 1")
            print(f"Actual result: {actual_result}")

    def test_multiplication_status_two(self):
        left = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_multiplication, data=json.dumps({"x": left}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 2:
            print()
            print("Expected result: 2")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 2")
            print(f"Actual result: {actual_result}")

    def test_multiplication_status_three(self):
        left = random.uniform(-2147483648, 2147483647)
        right = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_multiplication, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 3:
            print()
            print("Expected result: 3")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 3")
            print(f"Actual result: {actual_result}")

    def test_multiplication_status_four(self):
        left = random.randint(2147483647+3, 3000000000)
        right = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_multiplication, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 4:
            print()
            print("Expected result: 4")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 4")
            print(f"Actual result: {actual_result}")

    def test_multiplication_status_five(self):
        left = random.uniform(-2147483648, 2147483647)
        right = random.uniform(-2147483648, 21474836)
        dataset = requests.get(conf.url_multiplication, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 5:
            print()
            print("Expected result: 5")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 5")
            print(f"Actual result: {actual_result}")

    def test_choice_division_status_zero(self):
        left = random.randint(-2147483648, 2147483647)
        right = random.randint(-2147483648, left - 1)
        dataset = requests.post(conf.url_division, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 0:
            print()
            print("Expected result: 0")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 0")
            print(f"Actual result: {actual_result}")

    def test_division_status_two(self):
        left = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_division, data=json.dumps({"x": left}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 2:
            print()
            print("Expected result: 2")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 2")
            print(f"Actual result: {actual_result}")

    def test_division_status_three(self):
        left = random.uniform(-2147483648, 2147483647)
        right = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_division, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 3:
            print()
            print("Expected result: 3")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 3")
            print(f"Actual result: {actual_result}")

    def test_division_status_four(self):
        left = random.randint(2147483647+3, 3000000000)
        right = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_division, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 4:
            print()
            print("Expected result: 4")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 4")
            print(f"Actual result: {actual_result}")

    def test_division_status_five(self):
        left = random.uniform(-2147483648, 2147483647)
        right = random.uniform(-2147483648, 21474836)
        dataset = requests.get(conf.url_division, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 5:
            print()
            print("Expected result: 5")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 5")
            print(f"Actual result: {actual_result}")

    def test_choice_remainder_status_zero(self):
        left = random.randint(-2147483648, 2147483647)
        right = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_remainder, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 0:
            print()
            print("Expected result: 0")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print(f"Expected result: 0")
            print(f"Actual result: {actual_result}")

    def test_remainder_status_one(self):
        left = random.randint(-2147483648, 2147483647)
        right = 0
        dataset = requests.post(conf.url_remainder, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 1:
            print()
            print(f"Expected result: 1")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print(f"Expected result: 1")
            print(f"Actual result: {actual_result}")
            print(dataset.text)

    def test_remainder_status_two(self):
        left = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_remainder, data=json.dumps({"x": left}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 2:
            print()
            print("Expected result: 2")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 2")
            print(f"Actual result: {actual_result}")

    def test_remainder_status_three(self):
        left = random.uniform(-2147483648, 2147483647)
        right = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_remainder, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 3:
            print()
            print("Expected result: 3")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 3")
            print(f"Actual result: {actual_result}")

    def test_remainder_status_four(self):
        left = random.randint(2147483647+3, 3000000000)
        right = random.randint(-2147483648, 2147483647)
        dataset = requests.post(conf.url_remainder, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 4:
            print()
            print("Expected result: 4")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 4")
            print(f"Actual result: {actual_result}")

    def test_remainder_status_five(self):
        left = random.uniform(-2147483648, 2147483647)
        right = random.uniform(-2147483648, 21474836)
        dataset = requests.get(conf.url_remainder, data=json.dumps({"x": left, "y": right}))
        actual_result = dataset.json()['statusCode']
        if actual_result == 5:
            print()
            print("Expected result: 5")
            print(f"Actual result: {actual_result}")
            print(dataset.text)
        else:
            print()
            print("ERROR: Test is fail")
            print("Actual result is not equal to expected")
            print("Expected result: 5")
            print(f"Actual result: {actual_result}")



