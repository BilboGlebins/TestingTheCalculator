import random

class Configuration:

    url_state = "http://localhost:5413/api/state"
    url_addition = "http://localhost:5413/api/addition"
    url_multiplication = "http://localhost:5413/api/multiplication"
    url_division = "http://localhost:5413/api/division"
    url_remainder = "http://localhost:5413/api/remainder"

    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

    @staticmethod
    def integers():
        buff = random.randint(-2147483648, 2147483647)
        return buff

    @staticmethod
    def floating():
        buff = random.uniform(-2147483648, 2147483647)
        return buff

    @staticmethod
    def max_integers():
        buff = random.randint(2147483647+3, 3000000000)
        return buff

    @staticmethod
    def minority_integers(num):
        buff = random.randint(-2147483648, num - 1)
        return buff

    @staticmethod
    def more_integers(num):
        buff = random.randint(num+1, 2147483647)
        return buff

    @staticmethod
    def response_status(eresult, aresult, text):
        print()
        print(f"Expected result: {eresult}")
        print(f"Actual result: {aresult}")
        print(text)
        print()

    @staticmethod
    def response_function(num1, num2, eresult, aresult, text):
        print()
        print(f"Left number: {num1} | Right number: {num2}")
        print(f"Expected result: {eresult}")
        print(f"Actual result: {aresult}")
        print(text)
        print()

    @staticmethod
    def error_response_status(eresult, res, text):
        print()
        print("\033[31m" "ERROR: Test is fail")
        print("\033[31m" "Actual result is not equal to expected")
        print("\033[31m" f"Expected result: {eresult}")
        print("\033[31m" f"Actual result: {res}")
        print("\033[31m {}".format(text))
        print()

    @staticmethod
    def error_response_function(num1, num2, eresult, aresult, text):
        print()
        print("\033[31m" "ERROR: Test is fail")
        print("\033[31m" "Actual result is not equal to expected")
        print("\033[31m" f"Left number: {num1} | Right number: {num2}")
        print("\033[31m" f"Expected result: {eresult}")
        print("\033[31m" f"Actual result: {aresult}")
        print("\033[31m {}".format(text))
        print()

    @staticmethod
    def error_response_status(eresult, aresult, text):
        print()
        print("\033[31m" "ERROR: Test is fail")
        print("\033[31m" "Actual result is not equal to expected")
        print("\033[31m" f"Expected result: {eresult}")
        print("\033[31m" f"Actual result: {aresult}")
        print("\033[31m {}".format(text))
        print()
