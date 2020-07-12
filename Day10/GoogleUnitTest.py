import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner

class SearchTest(unittest.TestCase):

    #def setUp(self):
    @classmethod
    def setUpClass(cls):
            #Pre steps
        cls.driver = webdriver.Chrome(executable_path="D:\Webdriver\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    def test_1(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name('q').send_keys("Google")
        self.driver.find_element_by_name('q').send_keys(Keys.ENTER)
        print(self.driver.title)

    #Test2
    def test_2(self):
        self.driver.get("https://www.bing.com/")
        self.driver.find_element_by_name('q').send_keys("Microsoft")
        self.driver.find_element_by_name('q').send_keys(Keys.ENTER)
        print(self.driver.title)

    @classmethod
    #def tearDownClass(cls):
    #Post steps
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()




if __name__ == '__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Vignesh\\PycharmProjects\\Python_Tutorial\\reports"))
    unittest.main()