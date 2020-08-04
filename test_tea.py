import unittest
from selenium import webdriver
import time


class TestTea(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\Chrome\chromedriver')
        self.url = self.driver.get("http://www.practiceselenium.com/")

    def test_sea_collection_button(self):
        tea = self.driver.find_elements_by_xpath('//span[@class="button-content wsb-button-content"]')
        button_tea = []
        for i in tea:
            button_tea.append(i)
        button_tea[1].click()
        check_out_button = self.driver.find_elements_by_xpath('//span[@class="button-content wsb-button-content"]')
        button_check_out = []
        for i in check_out_button:
            button_check_out.append(i)
        button_check_out[2].click()
        e_mail_field = self.driver.find_element_by_xpath('//fieldset[1]//input[@id="email"]')
        e_mail_field.send_keys('artemkurchakov1018@gmail.com')
        name_field = self.driver.find_element_by_xpath('//fieldset[1]//input[@id="name"]')
        name_field.send_keys('Artem')
        address_field = self.driver.find_element_by_xpath('//fieldset[1]//textarea[@id="address"]')
        address_field.send_keys('Kharkiv')
        card_type = self.driver.find_element_by_xpath('//*[@id="card_type"]')
        card_type.click()
        mastercard = self.driver.find_element_by_xpath('//*[@id="card_type"]//option[3]')
        mastercard.click()
        card_number = self.driver.find_element_by_id("card_number")
        card_number.send_keys('123456789')
        cardholder_name = self.driver.find_element_by_id("cardholder_name")
        cardholder_name.send_keys('ABCD')
        verification_code = self.driver.find_element_by_id("verification_code")
        verification_code.send_keys('1018')
        place_order_button = self.driver.find_element_by_xpath('//button[@class="btn btn-primary"]')
        place_order_button.click()
        time.sleep(3)





    def tearDown(self):
        self.driver.close()