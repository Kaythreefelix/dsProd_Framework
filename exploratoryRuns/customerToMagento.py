import unittest
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
# import re


class CustomerFromMagento(unittest.TestCase):
    @classmethod
    def test_setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_customer_from_magento(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        #Nav to URL
        self.driver.get("https://dataswitch.k3imagine.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        #Login
        self.driver.find_element_by_id("name").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Testing552!")
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-k3").click()
        time.sleep(5)

        #Dashboard
        #self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Terms & Conditions'])[1]/following::button[1]").click()
        self.driver.find_element_by_link_text("Projects").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create a Dataflow'])[19]/following::div[3]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Copy API to clipboard'])[21]/following::div[6]").click()

        #Design Window
        self.driver.find_element_by_link_text("Execute").click()
        time.sleep(5)
        self.driver.find_element_by_id("testButtonIcon").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::button[3]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Dashboard'])[1]/preceding::span[1]").click()

        #Process Monitor
        self.driver.find_element_by_link_text("Process Monitor").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Are you sure you want to leave? Unsaved changes may be lost.'])[1]/following::button[1]").click()
        time.sleep(5)
        self.driver.find_element_by_id("show-success-resolved").click()
        time.sleep(7)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Total Processing Time'])[1]/following::div[40]").click()
        time.sleep(7)


        #Design Window(to View Results)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='POST Customers to Imagine'])[1]/following::div[2]").click()
        time.sleep(7)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='-'])[28]/following::i[1]").click()
        time.sleep(7)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Error Message'])[4]/following::button[2]").click()
        time.sleep(7)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::button[3]").click()
        time.sleep(7)
        self.driver.close()

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
