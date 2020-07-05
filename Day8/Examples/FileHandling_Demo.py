from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2, }
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/Webdriver/chromedriver.exe")

driver.get("http://leafground.com/pages/upload.html")
driver.implicitly_wait(30)

driver.find_element_by_name("filename").send_keys("C:\\Users\\Vignesh\\Desktop\\new.txt")

