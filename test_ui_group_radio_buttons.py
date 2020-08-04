import unittest
from selenium import webdriver


class RadioButton(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

    def test_male_zero_to_five(self):
        sex_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        sex_male.click()
        age_zero_to_five = self.driver.find_element_by_xpath('//input[@value="0 - 5"][@name="ageGroup"]')
        age_zero_to_five.click()
        get_values_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        get_values_button.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"][text()="Sex : Male"][text()=" Age group: 0 - 5"]')
        assert message.is_displayed()

    def test_male_five_to_fifteen(self):
        sex_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        sex_male.click()
        age_zero_to_five = self.driver.find_element_by_xpath('//input[@value="5 - 15"][@name="ageGroup"]')
        age_zero_to_five.click()
        get_values_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        get_values_button.click()
        message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Male"][text()=" Age group: 5 - 15"]')
        assert message.is_displayed()

    def test_male_fifteen_to_fifty(self):
        sex_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        sex_male.click()
        age_zero_to_five = self.driver.find_element_by_xpath('//input[@value="15 - 50"][@name="ageGroup"]')
        age_zero_to_five.click()
        get_values_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        get_values_button.click()
        message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Male"][text()=" Age group: 15 - 50"]')
        assert message.is_displayed()

    def test_female_zero_to_five(self):
        sex_male = self.driver.find_element_by_xpath('//input[@value="Female"][@name="gender"]')
        sex_male.click()
        age_zero_to_five = self.driver.find_element_by_xpath('//input[@value="0 - 5"][@name="ageGroup"]')
        age_zero_to_five.click()
        get_values_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        get_values_button.click()
        message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Female"][text()=" Age group: 0 - 5"]')
        assert message.is_displayed()

    def test_female_five_to_fifteen(self):
        sex_male = self.driver.find_element_by_xpath('//input[@value="Female"][@name="gender"]')
        sex_male.click()
        age_zero_to_five = self.driver.find_element_by_xpath('//input[@value="5 - 15"][@name="ageGroup"]')
        age_zero_to_five.click()
        get_values_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        get_values_button.click()
        message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Female"][text()=" Age group: 5 - 15"]')
        assert message.is_displayed()

    def test_female_fifteen_to_fifty(self):
        sex_male = self.driver.find_element_by_xpath('//input[@value="Female"][@name="gender"]')
        sex_male.click()
        age_zero_to_five = self.driver.find_element_by_xpath('//input[@value="15 - 50"][@name="ageGroup"]')
        age_zero_to_five.click()
        get_values_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        get_values_button.click()
        message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Female"][text()=" Age group: 15 - 50"]')
        assert message.is_displayed()

    def tearDown(self):
        self.driver.close()