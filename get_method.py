import unittest

from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_successful_registration_only_with_required_fields(self):
        self.browser.get(self.link)
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input")
        input_form.send_keys('Kirill')
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input")
        input_form.send_keys('Panchenko')
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input")
        input_form.send_keys('email@email.com')
        button = self.browser.find_element(By.TAG_NAME, "button")
        button.click()

        time.sleep(1)

        answer = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(answer.text, "Congratulations! You have successfully registered!")

    def test_successful_registration_with_all_fields(self):
        self.browser.get(self.link)
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input")
        input_form.send_keys('Kirill')
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input")
        input_form.send_keys('Panchenko')
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input")
        input_form.send_keys('email@email.com')
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.second_block div.first_class input")
        input_form.send_keys('666666666667')
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.second_block div.second_class input")
        input_form.send_keys('Mongolia, NY')
        button = self.browser.find_element(By.TAG_NAME, "button")
        button.click()

        time.sleep(1)

        answer = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(answer.text, "Congratulations! You have successfully registered!")

    def test_successful_registration_without_required_fields(self):
        self.browser.get(self.link)
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.second_block div.first_class input")
        input_form.send_keys('666666666667')
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.second_block div.second_class input")
        input_form.send_keys('Mongolia, NY')
        button = self.browser.find_element(By.TAG_NAME, "button")
        button.click()

        time.sleep(1)

        answer = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(answer.text, "Registration")
