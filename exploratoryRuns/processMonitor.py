import unittest
import time
import re
#import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProcMonitoProd(unittest.TestCase):
    def test_setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://dataswitch.k3imagine.com")
        #self.driver.get("https://dataswitch.k3imagine.com/#/login")


    def test_proc_monito_prod(self):
        driver = self.driver
        driver.get("https://dataswitch.k3imagine.com/#/login")
        driver.implicitly_wait(10)
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Testing552!")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Terms & Conditions'])[1]/following::button[1]").click()

        time.sleep(2)
        driver.find_element_by_link_text("Process Monitor").click()
        driver.find_element_by_name("filterByTime").click()
        Select(driver.find_element_by_name("filterByTime")).select_by_visible_text("Last week")
        driver.find_element_by_name("filterByTime").click()
        driver.find_element_by_id("show-success-resolved").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Total Processing Time'])[1]/following::div[40]").click()

        time.sleep(2)
        driver.find_element_by_link_text("Aaron Wilcock").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Are you sure you want to leave? Unsaved changes may be lost.'])[1]/following::button[1]").click()

        time.sleep(2)
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Testing552!")
#        driver.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    @classmethod
    def test_tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        # self.assertEqual([], self.verificationErrors)
        print('TEST COMPLETE')

if __name__ == "__main__":
    unittest.main(verbosity=2)