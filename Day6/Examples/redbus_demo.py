from selenium import webdriver
import time

#driver = webdriver.chrome(executable_path="D:/Webdriver/chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/Webdriver/chromedriver.exe")

driver.get("https://www.redbus.in/")
driver.find_element_by_id("src").send_keys("Kol")
time.sleep(3)
#srclist = driver.find_elements_by_tag_name("li")
#for s in srclist:
#    print(s.text)

srclist = driver.find_elements_by_xpath("//input[@id='src']/following-sibling::ul/li")
for s in srclist:
    print(s.text)
    #if s.text == "Dunlop, Kolkata":
    #    s.click()
    #    break
    #Contais
    if "Dunlop" in s.text:
        s.click()
        break