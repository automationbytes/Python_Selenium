from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
#driver = webdriver.chrome(executable_path="D:/Webdriver/chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/Webdriver/chromedriver.exe")
driver.set_page_load_timeout(90)
driver.get("https://www.irctc.co.in/")
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//button[text()='Ok']").click()

wait = WebDriverWait(driver,15,poll_frequency=5,ignored_exceptions="NoSuchElementException")
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Ok']")))
driver.find_element_by_xpath("//button[text()='Ok']").click()
