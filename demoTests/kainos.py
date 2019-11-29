import unittest
# import time
# import re
# import HtmlTestRunner
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
class FirstWebDriverTest(unittest.TestCase):
    def test_setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://www.allegro.pl")
        SEARCH_TEXT = "Laptop"
        SEARCH_FIELD_ID = "//input[@id='main-search-text']"
        SEARCH_BUTTON_ID = "//input[@class='search-btn']"
        SEARCH_RESULT_ITEM_TITLE = "//article[@class='offer offer-brand']//h2//span"
    def test_search_in_allegro_pl(self):
        driver = self.driver
        driver.find_element_by_xpath(self.SEARCH_FIELD_ID).send_keys(self.SEARCH_TEXT)
        driver.find_element_by_xpath(self.SEARCH_BUTTON_ID).submit()
        driver.implicitly_wait(5)
        driver.find_elements_by_xpath(self.SEARCH_RESULT_ITEM_TITLE)
        # .__getitem__(0)
        # .__getattribute__("text")
        # self.assertIn(self.SEARCH_TEXT, result)
    def test_tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TEST COMPLETE")


if __name__ == "__main__":
    unittest.main()