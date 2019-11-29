import unittest
import time
#import re
#import HtmlTestRunner
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC



class LoginLogoutProd(unittest.TestCase):
    @classmethod
    def test_setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_login_logout_prod(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("https://dataswitch.k3imagine.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("name").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Testing552!")
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-k3").click()
        time.sleep(2)

        self.driver.find_element_by_link_text("| Insights").click()
        time.sleep(7)
        self.driver.find_element_by_link_text("| Configuration").click()
        time.sleep(7)
        self.driver.find_element_by_link_text("| Administration").click()
        time.sleep(7)
        self.driver.find_element_by_link_text("Aaron Wilcock").click()
        time.sleep(7)
        self.driver.find_element_by_link_text("Aaron Wilcock").click()
        time.sleep(7)
        self.driver.find_element_by_link_text("Aaron Wilcock").click()
        time.sleep(7)
        time.sleep(7)
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(7)
        self.driver.find_element_by_id("name").clear()
        time.sleep(7)
        self.driver.find_element_by_id("name").send_keys("admin")
        time.sleep(7)
        self.driver.find_element_by_id("password").clear()
        time.sleep(7)
        self.driver.find_element_by_id("password").send_keys("Testing552!")




    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def is_alert_present(self):
    #     try:
    #         self.driver.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally:
    #         self.accept_next_alert = True

    @classmethod
    def test_tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        #self.assertEqual([], self.verificationErrors)
        print('TEST COMPLETE')


if __name__ == "__main__":
    unittest.main(verbosity=2)
