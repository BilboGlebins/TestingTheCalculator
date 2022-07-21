import time
from functions.start_functions import StartPage


class TestPlusFunctions:

    def test_correct_launch(self, driver):
        start_app = StartPage(driver, 'http://localhost:5413/api/state')
        start_app.open()
        start_app.correct_launch()

    def test_choice_addition(self, driver):
        start_app = StartPage(driver, 'http://localhost:5413/api/addition')
        start_app.open()
        start_app.choice_addition()

    def test_choice_multiplication(self, driver):
        start_app = StartPage(driver, 'http://localhost:5413/api/multiplication')
        start_app.open()
        start_app.choice_multiplication()

    def test_choice_division(self, driver):
        start_app = StartPage(driver, 'http://localhost:5413/api/division')
        start_app.open()
        start_app.choice_division()

    def test_choice_remainder(self, driver):
        start_app = StartPage(driver, 'http://localhost:5413/api/remainder')
        start_app.open()
        start_app.choice_remainder()



