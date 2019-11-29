import unittest
import time
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


class SearchText(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://www.google.com/")

    def test_search_by_text(self):
        self.search_field = self.driver.find_element_by_name("q")
        # self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()

        #
        # lists = self.driver.find_elements_by_class_name("r")
        # no=len(lists)
        # self.assertEqual(11, len(lists))
    @classmethod
    def tearDown(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print('TEST COMPLETE')

    if __name__ == "__main__":
            unittest.main(verbosity=2)
