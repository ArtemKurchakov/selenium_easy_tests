import unittest
from selenium import webdriver

class TestMultiSelectListDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

    def test_cities_text(self):
        all_cities = self.driver.find_elements_by_xpath('//select[@id="multi-select"]/option')
        cities_text = []
        for city in all_cities:
            cities_text.append(city.text)
        print(cities_text)
        assert len(cities_text) == 8, 'The number of cities in the list cities should be 8'

    def test_list_of_cities(self):
        all_cities = self.driver.find_elements_by_xpath('//select[@id="multi-select"]/option')
        cities = []
        for city in all_cities:
            cities.append(city)
        assert cities[0].is_displayed()
        assert cities[1].is_displayed()
        assert cities[2].is_displayed()
        assert cities[3].is_displayed()
        assert cities[4].is_displayed()
        assert cities[5].is_displayed()
        assert cities[6].is_displayed()
        assert cities[7].is_displayed()

    def test_first_selected_button(self):
        all_cities = self.driver.find_elements_by_xpath('//select[@id="multi-select"]/option')
        first_selected_button = self.driver.find_element_by_id("printMe")
        option_selected_message = self.driver.find_element_by_xpath('//p[@class="getall-selected"]')
        cities = []
        for city in all_cities:
            cities.append(city)
        cities[0].click()
        first_selected_button.click()
        assert option_selected_message.text == 'First selected option is : California', \
            'First selected option should be {}' .format(cities[0].text)
        cities[1].click()
        first_selected_button.click()
        assert option_selected_message.text == 'First selected option is : Florida', \
            'First selected option should be {}' .format(cities[1].text)
        cities[2].click()
        first_selected_button.click()
        assert option_selected_message.text == 'First selected option is : New Jersey', \
            'First selected option should be {}' .format(cities[2].text)
        cities[3].click()
        first_selected_button.click()
        assert option_selected_message.text == 'First selected option is : New York', \
            'First selected option should be {}' .format(cities[3].text)
        cities[4].click()
        first_selected_button.click()
        assert option_selected_message.text == 'First selected option is : Ohio', \
            'First selected option should be {}' .format(cities[4].text)
        cities[5].click()
        first_selected_button.click()
        assert option_selected_message.text == 'First selected option is : Texas', \
            'First selected option should be {}' .format(cities[5].text)
        cities[6].click()
        first_selected_button.click()
        assert option_selected_message.text == 'First selected option is : Pennsylvania', \
            'First selected option should be {}' .format(cities[6].text)
        cities[7].click()
        first_selected_button.click()
        assert option_selected_message.text == 'First selected option is : Washington', \
            'First selected option should be {}' .format(cities[7].text)

    def test_get_all_selected_button(self):
        all_cities = self.driver.find_elements_by_xpath('//select[@id="multi-select"]/option')
        get_all_selected_button = self.driver.find_element_by_id("printAll")
        option_selected_message = self.driver.find_element_by_xpath('//p[@class="getall-selected"]')
        cities = []
        for city in all_cities:
            cities.append(city)
        cities[0].click()
        get_all_selected_button.click()
        assert option_selected_message.text == 'Options selected are : California', \
            'The selected parameter should be {}' .format(cities[0].text)
        cities[1].click()
        get_all_selected_button.click()
        assert option_selected_message.text == 'Options selected are : Florida', \
            'The selected parameter should be {}' .format(cities[1].text)
        cities[2].click()
        get_all_selected_button.click()
        assert option_selected_message.text == 'Options selected are : New Jersey', \
            'The selected parameter should be {}' .format(cities[2].text)
        cities[3].click()
        get_all_selected_button.click()
        assert option_selected_message.text == 'Options selected are : New York', \
            'The selected parameter should be {}' .format(cities[3].text)
        cities[4].click()
        get_all_selected_button.click()
        assert option_selected_message.text == 'Options selected are : Ohio', \
            'The selected parameter should be {}' .format(cities[4].text)
        cities[5].click()
        get_all_selected_button.click()
        assert option_selected_message.text == 'Options selected are : Texas', \
            'The selected parameter should be {}' .format(cities[5].text)
        cities[6].click()
        get_all_selected_button.click()
        assert option_selected_message.text == 'Options selected are : Pennsylvania', \
            'The selected parameter should be {}' .format(cities[6].text)
        cities[7].click()
        get_all_selected_button.click()
        assert option_selected_message.text == 'Options selected are : Washington', \
            'The selected parameter should be {}' .format(cities[7].text)

    def test_no_city_selected(self):
        all_cities = self.driver.find_elements_by_xpath('//select[@id="multi-select"]/option')
        first_selected_button = self.driver.find_element_by_id("printMe")
        first_selected_button.click()
        option_selected_message = self.driver.find_element_by_xpath('//p[@class="getall-selected"]')
        assert option_selected_message.text == 'First selected option is : undefined'
        get_all_selected_button = self.driver.find_element_by_id("printAll")
        get_all_selected_button.click()
        assert option_selected_message.text == 'Options selected are :'

    def tearDown(self):
        self.driver.close()