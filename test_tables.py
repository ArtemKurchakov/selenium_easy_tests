import unittest
from selenium import webdriver


class TestTable(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/table-pagination-demo.html")

    def test_table_total_rows(self):
        table_rows = self.driver.find_elements_by_xpath('//tbody[@id="myTable"]//tr')
        assert len(table_rows) == 13

    def test_total_row_cells(self):
        all_cells = self.driver.find_elements_by_xpath('//tbody[@id="myTable"]//tr/td')
        assert len(all_cells) == 91

    def test_cell_name(self):
        all_cell = self.driver.find_elements_by_xpath('//tbody[@id="myTable"]//tr[2]/td')
        cell_names = []
        for names in all_cell:
            cell_names.append(names.text)
        assert cell_names[3] == 'Table cell'

    def test_table_heading(self):
        table_heading = self.driver.find_elements_by_xpath('//thead[@class="btn-primary"]//tr/th')
        assert len(table_heading) == 7

    def test_table_heading_five(self):
        all_table_heading = self.driver.find_elements_by_xpath('//thead[@class="btn-primary"]//tr/th')
        heading = []
        for name in all_table_heading:
            heading.append(name.text)
        assert heading[5] == 'Table heading 5', heading[5]

    def tearDown(self):
        self.driver.close()

