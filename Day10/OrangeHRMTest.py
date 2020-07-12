import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import time

class OrangeHRMTest(unittest.TestCase):
#setup

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="D:\Webdriver\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

    def test_logout(self):
        self.driver.find_element_by_id("welcome").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[text()='Logout']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Vignesh\\PycharmProjects\\Python_Tutorial\\reports"))
    #unittest.main()