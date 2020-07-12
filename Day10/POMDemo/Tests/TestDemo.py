import sys
import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import time
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

# import sys, os
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')

#from POMDemo.Locators.locators import Locators
from POMDemo.Pages.homePage import HomePage
from POMDemo.Pages.loginPage import LoginPage

class OrangeHRMTest(unittest.TestCase):
#driver: WebDriver

#setup

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="D:\Webdriver\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    def test_login(self):

        #driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        login = LoginPage(self.driver)
        #login = LoginPage(driver)

        login.enterUsername("Admin")
        login.enterPassword("admin123")
        login.clickLogin()

        homepage = HomePage(self.driver)
        homepage.clickWelcome()
        homepage.clickLogout()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Vignesh\\PycharmProjects\\Python_Tutorial\\reports"))
    #unittest.main()