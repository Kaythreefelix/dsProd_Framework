import unittest
import time
# import re
import HtmlTestRunner
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Ecom(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def test_ecom(self):
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.find_element_by_link_text("Sign in").click()
        self.driver.find_element_by_id("email").click()
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys("orofelix7@gmail.com")
        self.driver.find_element_by_id("passwd").clear()
        self.driver.find_element_by_id("passwd").send_keys("fTSw4M@wenb9TM@")
        self.driver.find_element_by_id("passwd").click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Forgot your password?'])[1]/following::span[1]").click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='My credit slips'])[1]/following::span[1]").click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='United States'])[1]/following::span[3]").click()
        self.driver.find_element_by_id("phone").click()
        self.driver.find_element_by_id("address1").clear()
        self.driver.find_element_by_id("address1").send_keys("6 Lydford Street")
        self.driver.find_element_by_id("postcode").clear()
        self.driver.find_element_by_id("postcode").send_keys("M6 6BJ")
        self.driver.find_element_by_id("postcode").click()
        self.driver.find_element_by_id("postcode").clear()
        self.driver.find_element_by_id("postcode").send_keys("90120")
        self.driver.find_element_by_id("phone").click()
        self.driver.find_element_by_id("phone").clear()
        self.driver.find_element_by_id("phone").send_keys("0738046732")
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='**'])[1]/following::div[2]").click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[10]/following::span[1]").click()
        time.sleep(2)
        self.driver.close()



    def tearDown(self):
        self.driver.quit()
#        self.assertEqual([], self.verificationErrors)
        print('TEST COMPLETED')


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output='C:/Users/filex.ebiye/PycharmProjects/dsProd_Framework/reports'))



#host:7942/api/v1.0/registration/token
#4d2180ca58ba46a5a9feb07846fc0caf---jenkins password








# class Ecom(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         # self.base_url = "https://www.katalon.com/"
#         # self.verificationErrors = []
#         # self.accept_next_alert = True
#
#     def test_ecom(self):
#         driver = self.driver
#         driver.get("http://automationpractice.com/index.php")
#         driver.find_element_by_link_text("Sign in").click()
#         driver.find_element_by_id("email").click()
#         driver.find_element_by_id("email").clear()
#         driver.find_element_by_id("email").send_keys("orofelix7@gmail.com")
#         driver.find_element_by_id("passwd").clear()
#         driver.find_element_by_id("passwd").send_keys("fTSw4M@wenb9TM@")
#         driver.find_element_by_id("passwd").click()
#         driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Forgot your password?'])[1]/following::span[1]").click()
#         driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='My credit slips'])[1]/following::span[1]").click()
#         driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='United States'])[1]/following::span[3]").click()
#         driver.find_element_by_id("phone").click()
#         driver.find_element_by_id("address1").clear()
#         driver.find_element_by_id("address1").send_keys("6 Lydford Street")
#         driver.find_element_by_id("postcode").clear()
#         driver.find_element_by_id("postcode").send_keys("M6 6BJ")
#         driver.find_element_by_id("postcode").click()
#         driver.find_element_by_id("postcode").clear()
#         driver.find_element_by_id("postcode").send_keys("90120")
#         driver.find_element_by_id("phone").click()
#         driver.find_element_by_id("phone").clear()
#         driver.find_element_by_id("phone").send_keys("0738046732")
#         driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='**'])[1]/following::div[2]").click()
#         driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[10]/following::span[1]").click()
#         time.sleep(2)
#         driver.close()
#
#     # def is_element_present(self, how, what):
#     #     try:
#     #         self.driver.find_element(by=how, value=what)
#     #     except NoSuchElementException as e:
#     #         return False
#     #     return True
#     #
#     # def is_alert_present(self):
#     #     try:
#     #         self.driver.switch_to_alert()
#     #     except NoAlertPresentException as e:
#     #         return False
#     #     return True
#     #
#     # def close_alert_and_get_its_text(self):
#     #     try:
#     #         alert = self.driver.switch_to_alert()
#     #         alert_text = alert.text
#     #         if self.accept_next_alert:
#     #             alert.accept()
#     #         else:
#     #             alert.dismiss()
#     #         return alert_text
#     #     finally:
#     #         self.accept_next_alert = True
#
#     def tearDown(self):
#         self.driver.quit()
# #        self.assertEqual([], self.verificationErrors)
#         print('TEST COMPLETED')
#
#
# if __name__ == "__main__":
#     unittest.main()