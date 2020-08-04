import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestGetRandomUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")

    def test_get_random_user_first(self):
        button = self.driver.find_element_by_xpath('//button[@id="save"]')
        button.click()
        image = self.driver.find_element_by_xpath('//div[@id="loading"]/img')
        all_info = self.driver.find_element_by_xpath('//div[@id="loading"]')
        waiting_for_download = WebDriverWait(self.driver, 2)
        waiting_for_download.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="loading"]/img')))
        waiting_for_download.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="loading"]')))
        print(image.is_displayed())
        print(all_info.is_displayed())
        assert image.is_displayed()
        assert all_info.is_displayed()

    def test(self):
        button = self.driver.find_element_by_xpath('//button[@id="save"]')
        button.click()
        waiting_for_download = WebDriverWait(self.driver, 5)
        waiting_for_download.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Name')]")))
        name = self.driver.find_element_by_xpath("//div[contains(text(), 'Name')]")
        print(name)
        print(type(name))

    def test_get_random_user_second(self):
        button = self.driver.find_element_by_xpath('//button[@id="save"]')
        button.click()
        time.sleep(2)
        image = self.driver.find_element_by_xpath('//div[@id="loading"]/img')
        assert image.is_displayed()
        print(image.is_displayed())
        print(image.get_attribute('src'))
        print(type(image))

    def test_get_random_user_all_info(self):
        button = self.driver.find_element_by_xpath('//button[@id="save"]')
        button.click()
        time.sleep(1)
        all_info = self.driver.find_element_by_xpath('//div[@id="loading"]')
        assert all_info.is_displayed()
        print(all_info.is_displayed())

    def tearDown(self):
        self.driver.close()
