import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")

    def test_filter_data_by_seo(self):
        wait_input = WebDriverWait(self.driver, 5)
        input_line = self.driver.find_element_by_id('task-table-filter')
        input_line.send_keys('seo')
        seo = self.driver.find_element_by_xpath('//*[@id="task-table"]/tbody/tr[3]')
        assert seo.is_displayed()

    def test_filter_data_by_wirewframes(self):
        input_line = self.driver.find_element_by_id('task-table-filter')
        input_line.send_keys('wireframes')
        wireframes = self.driver.find_element_by_xpath('//*[@id="task-table"]/tbody/tr[1]')
        assert wireframes.is_displayed()

    def test_filter_data_by_two_words(self):
        input_line = self.driver.find_element_by_id('task-table-filter')
        input_line.send_keys('kilgore trout')
        kilgore_trout = self.driver.find_element_by_xpath('//*[@id="task-table"]/tbody/tr[7]')
        assert kilgore_trout.is_displayed()

    def test_filter_data_three_meanings(self):
        input_line = self.driver.find_element_by_id('task-table-filter')
        input_line.send_keys('in progress')
        first_meaning = self.driver.find_element_by_xpath('//table[@id="task-table"]/tbody/tr[1]')
        second_meaning = self.driver.find_element_by_xpath('//table[@id="task-table"]/tbody/tr[4]')
        third_meaning = self.driver.find_element_by_xpath('//table[@id="task-table"]/tbody/tr[7]')
        assert first_meaning.is_displayed()
        assert second_meaning.is_displayed()
        assert third_meaning.is_displayed()

    def test_filter_data_no_results_found(self):
        input_line = self.driver.find_element_by_id('task-table-filter')
        input_line.send_keys('11')
        no_results_found = self.driver.find_element_by_xpath('//*[@id="task-table"]/tbody/tr[8]/td')
        assert no_results_found.is_displayed()



    def test_wireframes(self):
        input_line = self.driver.find_element_by_id('task-table-filter')
        input_line.send_keys('in p')
        table_of_sorted_values = self.driver.find_elements_by_xpath('//table[@id="task-table"]//tbody//tr[1]/td')
        table_new = []
        for elements in table_of_sorted_values:
            table_new.append(elements.text)
        assert table_new[1] == 'Wireframes'

    def test_number_of_columns(self):
        input_line = self.driver.find_element_by_id('task-table-filter')
        input_line.send_keys('in p')
        table = self.driver.find_elements_by_xpath('//table[@id="task-table"]/tbody/tr[not(contains(@style, "display: none;"))]')
        assert len(table) == 3
        print(table)


    def tearDown(self):
        self.driver.close()

