import unittest
import time
# import re
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

class StockLevelsImagineProj(unittest.TestCase):

    @classmethod
    def test_setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        #cls.driver.get("https://dataswitch.k3imagine.com")


    def test_stock_levels_imagine_proj(self):
        self.driver.get("https://dataswitch.k3imagine.com")
        #self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("name").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Testing552!")
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-k3").click()

    #
    # def test_process_monitor(self):
    #     #self.driver.implicitly_wait(10)
    #     self.driver.find_element_by_link_text("Process Monitor").click()
    #     self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Are you sure you want to leave? Unsaved changes may be lost.'])[1]/following::button[1]").click()
    #     self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Stock Levels from Imagine'])[1]/following::div[2]").click()
    #     self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::button[3]").click()


    # def test_logout(self):
    #     self.driver.find_element_by_link_text("Aaron Wilcock").click()
    #     self.driver.find_element_by_link_text("Logout").click()
    #     self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Are you sure you want to leave? Unsaved changes may be lost.'])[1]/following::button[1]").click()
    #     self.driver.find_element_by_id("name").clear()
    #     self.driver.find_element_by_id("name").send_keys("admin")
    #     self.driver.find_element_by_id("password").clear()
    #     self.driver.find_element_by_id("password").send_keys("Testing552!")

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
        # self.assertEqual([], self.verificationErrors)
        print('TEST COMPLETE')

if __name__ == "__main__":
    unittest.main(verbosity=2)