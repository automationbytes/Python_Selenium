from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")

driver.get("https://www.facebook.com/")
#driver.find_element_by_id("email").send_keys("test@facebook.com")
#driver.find_element_by_id("pass").send_keys("test")

#driver.find_element_by_name("email").send_keys("abc@facecbook.com")
#driver.find_element_by_name("pass").send_keys("ABC")

#driver.find_element_by_class_name("inputtext _55r1 _6luy").send_keys("Hello")
#driver.find_element_by_link_text("Help").click()
#driver.find_element_by_partial_link_text("login").click()

driver.find_element_by_xpath("//input[@name='email']").send_keys("Hello@facebook.com")