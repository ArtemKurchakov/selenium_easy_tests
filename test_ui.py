import unittest
from selenium import webdriver


class SeleniumEasy(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

    def test_display_message(self):
        enter_message_field = self.driver.find_element_by_xpath('//div[@class="form-group"]//input[@id="user-message"]')
        enter_message_field.send_keys('hello')

        close_button = self.driver.find_element_by_id('at-cv-lightbox-close')
        close_button.click()

        show_message_button = self.driver.find_element_by_xpath('//button[contains(text(), "Show Message")]')
        show_message_button.click()

        your_message = self.driver.find_element_by_xpath('//span[contains(text(), "hello")]')
        assert your_message.is_displayed()

    def test_total(self):
        enter_a_field = self.driver.find_element_by_id('sum1')
        enter_a_field.send_keys('5')

        enter_b_field = self.driver.find_element_by_id('sum2')
        enter_b_field.send_keys('5')

        get_total_button = self.driver.find_element_by_xpath('//button[contains(text(), "Get Total")]')
        get_total_button.click()

        total = self.driver.find_element_by_xpath('//span[contains(text(), "10")]')
        assert total.is_displayed()


    def tearDown(self):
        self.driver.close()