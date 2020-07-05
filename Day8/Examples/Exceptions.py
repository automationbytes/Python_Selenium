from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(30)
driver.quit()
driver.get("https://jqueryui.com/droppable/")