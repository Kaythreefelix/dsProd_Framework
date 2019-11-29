import unittest
import time
import re
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePageDashboard(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_home_page_dashboard(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        #Nav to URL
        self.driver.get("https://dataswitch.k3imagine.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #Login
        self.driver.find_element_by_id("name").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Testing552!")
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-k3").click()
        time.sleep(5)
        #Nav to Projects
       # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Dashboard'])[1]/following::a[4]").click()

        self.driver.find_element_by_link_text("| Insights").click()
        time.sleep(5)
        self.driver.find_element_by_link_text("| Configuration").click()
        time.sleep(5)
        self.driver.find_element_by_link_text("| Administration").click()
        time.sleep(5)


        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Last Logged In : Oct 14, 2019 - 7:59 AM'])[1]/following::button[1]").click()
        # time.sleep(5)
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select a Project'])[2]/following::span[1]").click()
        # time.sleep(5)
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select a Project'])[2]/following::span[1]").click()
        # time.sleep(5)
        #
        # self.driver.find_element_by_link_text("Aaron Wilcock").click()
        # time.sleep(5)
        # self.driver.find_element_by_link_text("Profile").click()
        # time.sleep(5)
        # self.driver.find_element_by_link_text("Aaron Wilcock").click()
        # time.sleep(5)
        # self.driver.find_element_by_link_text("Logout").click()
        # time.sleep(5)
        # self.driver.find_element_by_id("name").clear()
        # time.sleep(5)
        # self.driver.find_element_by_id("name").send_keys("admin")
        # time.sleep(5)
        # self.driver.find_element_by_id("password").clear()
        # time.sleep(5)
        # self.driver.find_element_by_id("password").send_keys("Testing552!")
        # time.sleep(5)
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
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        #self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output='C:/Users/filex.ebiye/PycharmProjects/dsProd_Framework/reports'))
