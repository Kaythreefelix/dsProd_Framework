import unittest
import time
from selenium import webdriver


class ProdE2E(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/filex.ebiye/PycharmProjects/dsProd_Framework/drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login(self):
        self.driver.get("https://dataswitch.k3imagine.com")
        time.sleep(5)
        self.driver.find_element_by_id("name").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Testing552!")
        time.sleep(5)
        self.driver.find_element_by_class_name("btn-k3").click()
        time.sleep(5)
        # self.assertEqual(True, False)


        #Dashboard

    #def test_processmonitor_insight(self):
        #self.driver.find_element_by_partial_link_text("Process Monitor").click() #process monitor
        #self.driver.find_element_by_class_name("show-success-resolved").click() #show all
        #self.driver.find_element_by_id("dx-col-1").click() #data flow name row
        #self.driver.find_element_by_class_name("dx-selection").click() #pagination

    #def test_configuration_projects(self):
        self.driver.find_element_by_partial_link_text("Projects").click() #project menu
        time.sleep(5)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create a Dataflow'])[19]/following::i[1]").click() #project name
        time.sleep(5)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create a Dataflow'])[20]/following::h5[1]").click()#products to magento
        time.sleep(5)
        self.driver.find_element_by_link_text("Execute").click() #dataflow design window
        time.sleep(5)
        self.driver.find_element_by_id("testButtonIcon").click() #execute dataflow
        time.sleep(5)
        #self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::button[3]").click()
        time.sleep(10)
        self.driver.find_element_by_class_name("btn-success").click()
        time.sleep(5)

    # def test_something(self):
    # def test_something(self):
    # def test_something(self):
    # def test_something(self):

    @classmethod
    def test_tearDown(cls):
        time.sleep(10)
        cls.driver.close()
        #cls.driver.quite()


if __name__ == '__main__':
    unittest.main(verbosity=2)



#        driver.get("https://dataswitch.k3imagine.com/#/login")
  #      driver.find_element_by_id("name").clear()
        # driver.find_element_by_id("name").send_keys("admin")
        # driver.find_element_by_id("password").send_keys("Testing552!")
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Terms & Conditions'])[1]/following::button[1]").click()
        # driver.find_element_by_link_text("Projects").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create a Dataflow'])[19]/following::i[1]").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create a Dataflow'])[20]/following::h5[1]").click()
        # driver.find_element_by_link_text("Execute").click()
        # driver.find_element_by_id("testButtonIcon").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::button[3]").click()
        # driver.close()