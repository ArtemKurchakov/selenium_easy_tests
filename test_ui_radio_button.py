import unittest
from selenium import webdriver


class RadioButton(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

    def test_radio_button_demo_male(self):
        button = self.driver.find_elements_by_xpath('//label[@class="radio-inline"]//input[@name="optradio"]')
        button_list = []
        for element in button:
            button_list.append(element)

        button_male = button_list[0].click()
        button_get_check_value = self.driver.find_element_by_id('buttoncheck').click()
        message_male = self.driver.find_element_by_xpath('//p[contains(text(), "Male")]')
        assert message_male.is_displayed()

    def test_radio_button_demo_female(self):
        button = self.driver.find_elements_by_xpath('//label[@class="radio-inline"]//input[@name="optradio"]')
        button_list = []
        for element in button:
            button_list.append(element)

        button_female = button_list[1].click()
        button_get_check_value = self.driver.find_element_by_id('buttoncheck').click()
        message_female = self.driver.find_element_by_xpath('//p[contains(text(), "Female")]')
        assert message_female.is_displayed()


    def tearDown(self):
        self.driver.close()