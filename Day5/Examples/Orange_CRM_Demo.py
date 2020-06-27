from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//input[@name='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//input[@name='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//input[@name='Submit']").click()
#driver.close()
#driver.quit()
driver.get("https://www.google.com")
driver.fullscreen_window()

print(driver.title)
print(driver.current_url)
