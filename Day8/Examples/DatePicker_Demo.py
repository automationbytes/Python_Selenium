from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/Webdriver/chromedriver.exe")

driver.get("https://www.redbus.in")
driver.implicitly_wait(30)

driver.find_element_by_id("src").send_keys("Chennai")
time.sleep(2)
srclist = driver.find_elements_by_xpath("//input[@id='src']/parent::div//li")
for s in srclist:
    print (s.text)
    if "Airport" in s.text:
        s.click()
        break
time.sleep(2)
driver.find_element_by_id("onward_cal").click()
for i in range(12):
    MonthTitle = driver.find_element_by_xpath("//td[@class='monthTitle']")
    if MonthTitle.text == "Dec 2020":
        srccalendar = driver.find_elements_by_xpath("//table[@class='rb-monthTable first last']/tbody/tr/td")
        for cal in srccalendar:
            print(cal.text)
            if cal.text == '19':
                cal.click()
                break
        break
    else:
        driver.find_element_by_xpath("//td[@class='next']/button").click()

driver.save_screenshot("c:/vignesh/screenshot.png")
driver.get_screenshot_as_png()