import unittest
from selenium import webdriver


class TestGetRandomUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

    def test_select_list_demo_sunday(self):
        select_a_day = self.driver.find_element_by_id("select-demo")
        select_a_day.find_element_by_xpath('//select/option[@value="Sunday"]').click()
        day_selected = self.driver.find_element_by_xpath('//p[@class="selected-value"]')
        assert day_selected.text == 'Day selected :- Sunday'

    def test_select_list_demo_monday(self):
        select_a_day = self.driver.find_element_by_id("select-demo")
        select_a_day.find_element_by_xpath('//select/option[@value="Monday"]').click()
        day_selected = self.driver.find_element_by_xpath('//p[@class="selected-value"]')
        assert day_selected.text == 'Day selected :- Monday'

    def test_select_list_demo_tuesday(self):
        select_a_day = self.driver.find_element_by_id("select-demo")
        select_a_day.find_element_by_xpath('//select/option[@value="Tuesday"]').click()
        day_selected = self.driver.find_element_by_xpath('//p[@class="selected-value"]')
        assert day_selected.text == 'Day selected :- Tuesday'

    def test_select_list_demo_wednesday(self):
        select_a_day = self.driver.find_element_by_id("select-demo")
        select_a_day.find_element_by_xpath('//select/option[@value="Wednesday"]').click()
        day_selected = self.driver.find_element_by_xpath('//p[@class="selected-value"]')
        assert day_selected.text == 'Day selected :- Wednesday'

    def test_select_list_demo_thursday(self):
        select_a_day = self.driver.find_element_by_id("select-demo")
        select_a_day.find_element_by_xpath('//select/option[@value="Thursday"]').click()
        day_selected = self.driver.find_element_by_xpath('//p[@class="selected-value"]')
        assert day_selected.text == 'Day selected :- Thursday'

    def test_select_list_demo_friday(self):
        select_a_day = self.driver.find_element_by_id("select-demo")
        select_a_day.find_element_by_xpath('//select/option[@value="Friday"]').click()
        day_selected = self.driver.find_element_by_xpath('//p[@class="selected-value"]')
        assert day_selected.text == 'Day selected :- Friday'

    def test_select_list_demo_saturday(self):
        select_a_day = self.driver.find_element_by_id("select-demo")
        select_a_day.find_element_by_xpath('//select/option[@value="Saturday"]').click()
        day_selected = self.driver.find_element_by_xpath('//p[@class="selected-value"]')
        assert day_selected.text == 'Day selected :- Saturday'

    def test_as_list(self):
        all_days = self.driver.find_elements_by_xpath('//select[@class="form-control"]/option')
        day_selected = self.driver.find_element_by_xpath('//p[@class="selected-value"]')
        day = []
        for i in all_days:
            day.append(i)
        sunday = day[1].click()
        assert day_selected.text == 'Day selected :- Sunday', \
            'This item in the list should be {}' .format(day[1].text)
        monday = day[2].click()
        assert day_selected.text == 'Day selected :- Monday', \
            'This item in the list should be {}' .format(day[2].text)
        tuesday = day[3].click()
        assert day_selected.text == 'Day selected :- Tuesday', \
            'This item in the list should be {}' .format(day[3].text)
        wednesday = day[4].click()
        assert day_selected.text == 'Day selected :- Wednesday', \
            'This item in the list should be {}' .format(day[4].text)
        thursday = day[5].click()
        assert day_selected.text == 'Day selected :- Thursday', \
            'This item in the list should be {}' .format(day[5].text)
        friday = day[6].click()
        assert day_selected.text == 'Day selected :- Friday', \
            'This item in the list should be {}' .format(day[6].text)
        saturday = day[7].click()
        assert day_selected.text == 'Day selected :- Saturday', \
            'This item in the list should be {}' .format(day[7].text)


    def tearDown(self):
        self.driver.close()