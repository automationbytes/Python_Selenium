from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
driver.implicitly_wait(30)

driver.find_element_by_xpath('//a[@onclick="retheme()"]').click()
time.sleep(3)
#driver.switch_to.frame("iframeResult")
#driver.switch_to.frame(0)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='iframeResult']"))
#driver.switch_to_frame()
driver.find_element_by_xpath("//button[text()='Try it']").click()
driver.switch_to.default_content()
driver.find_element_by_xpath('//a[@onclick="retheme()"]').click()
time.sleep(3)

#driver.switch_to.parent_frame()