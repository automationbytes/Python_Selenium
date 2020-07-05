from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/Webdriver/chromedriver.exe")
'''
driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.implicitly_wait(30)

pnrstatus = driver.find_element_by_xpath("//*[text()='PNR STATUS']")
driver.execute_script("arguments[0].click();",pnrstatus)
'''

driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)

custom = driver.find_element_by_xpath("//*[text()='മലയാളം']")
driver.execute_script("arguments[0].click();",custom)