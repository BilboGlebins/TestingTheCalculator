import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from functions.base_function import BasePage
from locators.calculator_locators import CalculatorLocators as Locators


class StartPage(BasePage):

    def correct_launch(self):
        time.sleep(2)
        text_answer = self.driver.find_element(*Locators.STATUSZERO)
        if text_answer is None:
            print("ERROR: Element not found")
        else:
            print("Application launch correct")

    def choice_addition(self):
        time.sleep(2)
        text_answer = self.driver.find_element(*Locators.STATUSFIVEADD)
        if text_answer is None:
            print("ERROR: Element not found")
        else:
            print("Choice function addition")

    def choice_multiplication(self):
        time.sleep(2)
        text_answer = self.driver.find_element(*Locators.STATUSFIVEMULT)
        if text_answer is None:
            print("ERROR: Element not found")
        else:
            print("Choice function multiplication")

    def choice_division(self):
        time.sleep(2)
        text_answer = self.driver.find_element(*Locators.STATUSFIVEDIVIS)
        if text_answer is None:
            print("ERROR: Element not found")
        else:
            print("Choice function division")

    def choice_remainder(self):
        time.sleep(2)
        text_answer = self.driver.find_element(*Locators.STATUSFIVEREMIN)
        if text_answer is None:
            print("ERROR: Element not found")
        else:
            print("Choice function remainder")









