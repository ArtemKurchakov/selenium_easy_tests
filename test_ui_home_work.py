import unittest
from selenium import webdriver


class SeleniumHome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

    def test_single_checkbox(self):
        click_checkbox = self.driver.find_element_by_id('isAgeSelected')
        click_checkbox.click()

        show_message = self.driver.find_element_by_id('txtAge')
        assert show_message.is_displayed()

    def test_multiple_checkbox_button_uncheck(self):
        button_check = self.driver.find_element_by_id('check1')
        button_check.click()
        option = self.driver.find_elements_by_xpath('//div[@class="panel-body"]//div[@class="checkbox"]//input[@class="cb1-element"]')
        option_list = []
        for element in option:
            option_list.append(element)

        option_one = option_list[0].is_selected()
        option_two = option_list[1].is_selected()
        option_three = option_list[2].is_selected()
        option_four = option_list[3].is_selected()

        check_uncheck_button_value = button_check.get_attribute('value') == 'Uncheck All'

        # click_option_one = self.driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label').is_selected()
        # click_option_two = self.driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label').is_selected()
        # click_option_three = self.driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label').is_selected()
        # click_option_four = self.driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[4]/label').is_selected()
        # show = button_check.get_attribute('value')

    def test_multiple_checkbox_button_check(self):
        button_check = self.driver.find_element_by_id('check1')
        button_check.click()

        option = self.driver.find_elements_by_xpath('//div[@class="panel-body"]//div[@class="checkbox"]//input[@class="cb1-element"]')
        option_list = []
        for element in option:
            option_list.append(element)
        option_one = option_list[0].click()
        # self.driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label').click()

        assert button_check.get_attribute('value') == 'Check All', "Attribute value is not check all"


    def tearDown(self):
        self.driver.close()