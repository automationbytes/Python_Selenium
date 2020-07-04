from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.openmultipleurl.com/")
driver.implicitly_wait(30)
driver.find_element_by_id("list_urls").send_keys("https://www.google.com")
driver.find_element_by_id("list_urls").send_keys(Keys.ENTER)
driver.find_element_by_id("list_urls").send_keys("https://www.bing.com")
driver.find_element_by_id("list_urls").send_keys(Keys.ENTER)
driver.find_element_by_id("list_urls").send_keys("https://www.yahoo.com")
driver.find_element_by_id("list_urls").send_keys(Keys.ENTER)
driver.find_element_by_id("list_urls").send_keys("https://www.facebook.com")
driver.find_element_by_id("list_urls").send_keys(Keys.ENTER)
driver.find_element_by_xpath("//input[@value='Go Now']").click()
###### Window Handling##############
parentwindow = driver.current_window_handle
print(parentwindow)
print(driver.title)
print(driver.current_url)
allwindows = driver.window_handles
# in java - set and in python its list
print(type(allwindows))
print(len(allwindows))
'''for a in allwindows:
    print(a)
    if a != parentwindow:
        driver.switch_to.window(a)
        print(driver.title) 
        print(driver.current_url)
        time.sleep(3)
        driver.close()
'''
for a in allwindows:
    print(a)
    if a!= parentwindow:
        driver.switch_to.window(a)
        #print(a.title())
        if 'Google' in driver.title:
            driver.find_element_by_xpath('//input[@maxlength="2048"]').send_keys("Selenium Multiple Windows Handling")
            time.sleep(15)
        else:
            print(driver.title)
            driver.close()
driver.switch_to.window(parentwindow)
driver.close()