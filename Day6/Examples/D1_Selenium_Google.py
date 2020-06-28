from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")

driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//input[@aria-label = 'First name']").clear()
driver.find_element_by_xpath("//input[@aria-label = 'First name']").send_keys("TestName")
driver.find_element_by_xpath("//input[@name='lastname']").send_keys("TestSurName")
driver.find_element_by_xpath("//input[@value='2']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[text()='Create a Page']").click()
