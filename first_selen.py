import math
import os.path
import unittest

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self) -> None:
        time.sleep(5)
        self.browser.quit()

    def test_successful_registration_without_required_fields(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.second_block div.first_class input")
        input_form.send_keys('666666666667')
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.second_block div.second_class input")
        input_form.send_keys('Mongolia, NY')
        button = self.browser.find_element(By.TAG_NAME, "button")
        button.click()
        answer = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(answer.text, "Registration")

    def test_one(self):
        link = "http://suninjuly.github.io/math.html"
        self.browser.get(link)
        x = self.browser.find_element(By.ID, "input_value").text
        input_form = self.browser.find_element(By.ID, "answer")
        input_form.send_keys(calc(x))
        checkbox = self.browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
        checkbox.click()
        radio = self.browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
        radio.click()
        button = self.browser.find_element(By.TAG_NAME, 'button')
        button.click()

    def test_two(self):
        link = 'http://suninjuly.github.io/get_attribute.html'
        self.browser.get(link)
        img = self.browser.find_element(By.ID, 'treasure')
        valuex = img.get_attribute("valuex")
        x = calc(valuex)
        input_form = self.browser.find_element(By.ID, "answer")
        input_form.send_keys(x)
        checkbox = self.browser.find_element(By.ID, 'robotCheckbox')
        checkbox.click()
        radio = self.browser.find_element(By.ID, 'robotsRule')
        radio.click()
        button = self.browser.find_element(By.TAG_NAME, 'button')
        button.click()

    def test_three(self):
        link = 'http://suninjuly.github.io/selects1.html'
        self.browser.get(link)
        num1 = self.browser.find_element(By.ID, "num1").text
        # operation = self.browser.find_element(By.CSS_SELECTOR, "h2 span:nth-of-type(3)")
        num2 = self.browser.find_element(By.ID, "num2").text
        select = Select(self.browser.find_element(By.TAG_NAME, 'select'))
        select.select_by_value(f'{int(num2) + int(num1)}')
        button = self.browser.find_element(By.TAG_NAME, 'button')
        button.click()

    def test_four(self):
        link = "https://SunInJuly.github.io/execute_script.html"
        self.browser.get(link)
        x = self.browser.find_element(By.ID, "input_value").text
        input_form = self.browser.find_element(By.ID, "answer")
        input_form.send_keys(calc(x))
        checkbox = self.browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
        checkbox.click()
        radio = self.browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
        radio.click()
        button = self.browser.find_element_by_tag_name("button")
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    def test_five(self):
        link = "http://suninjuly.github.io/file_input.html"
        self.browser.get(link)
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.form-group input:nth-of-type(1)")
        input_form.send_keys('kirill')
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.form-group input:nth-of-type(2)")
        input_form.send_keys('kirill')
        input_form = self.browser.find_element(By.CSS_SELECTOR, "div.form-group input:nth-of-type(3)")
        input_form.send_keys('email')
        input_form = self.browser.find_element(By.ID, 'file')
        with open('file.txt', "w") as f:
            pass
        path = os.path.abspath('file.txt')
        input_form.send_keys(path)
        self.browser.find_element(By.TAG_NAME, "button").click()

    def test_alert(self):
        link = 'http://suninjuly.github.io/alert_accept.html'
        self.browser.get(link)
        button = self.browser.find_element(By.TAG_NAME, 'button')
        button.click()
        confirm = self.browser.switch_to.alert
        confirm.accept()
        x = self.browser.find_element(By.ID, "input_value").text
        input_frame = self.browser.find_element(By.ID, "answer")
        input_frame.send_keys(calc(x))
        self.browser.find_element(By.TAG_NAME, "button").click()

    def test_switch_to_new_window(self):
        link = "http://suninjuly.github.io/redirect_accept.html"
        self.browser.get(link)
        self.browser.find_element(By.TAG_NAME, "button").click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        x = self.browser.find_element(By.ID, "input_value").text
        input_frame = self.browser.find_element(By.ID, "answer")
        input_frame.send_keys(calc(x))
        self.browser.find_element(By.TAG_NAME, "button").click()

    def test_buy_house(self):
        link = 'http://suninjuly.github.io/explicit_wait2.html'
        self.browser.get(link)
        WebDriverWait(self.browser, 12).until(
            expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))
        self.browser.find_element_by_id('book').click()
        x = self.browser.find_element(By.ID, "input_value").text
        input_frame = self.browser.find_element(By.ID, "answer")
        input_frame.send_keys(calc(x))
        self.browser.find_element(By.ID, "solve").click()

