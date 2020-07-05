from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.redbus.in/")
driver.implicitly_wait(30)
'''
#Scrolling Down
driver.execute_script("window.scrollBy(0,1000);") #width,height
#in this eg, width = 0 and height = 1000
time.sleep(10)
#Scrolling up
driver.execute_script("window.scrollBy(0,-500);")

#Scrolling left to right
driver.execute_script("window.scrollBy(100,0);") #width,height
#in this eg, width = 0 and height = 1000
time.sleep(10)
#Scrolling up
driver.execute_script("window.scrollBy(-100,0);")

#Scrolling to bottom of the page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#Scrolling to up
driver.execute_script("window.scrollTo(0,-document.body.scrollHeight);")
'''
#Scroll to element level -
locator = driver.find_element_by_id("sendLinkButton")
driver.execute_script("arguments[0].scrollIntoView(true);",locator)