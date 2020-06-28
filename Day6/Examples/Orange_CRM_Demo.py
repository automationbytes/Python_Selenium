from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//input[@name='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//input[@name='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//input[@name='Submit']").click()
time.sleep(2)
#driver.find_element_by_id("menu_leave_viewLeaveModule").click()
#driver.find_element_by_id("leaveList_chkSearchFilter_checkboxgroup_allcheck").click()

driver.find_element_by_link_text("Recruitment").click()
#select = Select(driver.find_element_by_id("candidateSearch_jobTitle"))
select = Select(driver.find_element_by_xpath("//select[@id='candidateSearch_jobTitle']"))
#select.select_by_visible_text("IT Manager")
#select.select_by_index(3)
select.select_by_value("9")
time.sleep(5)
select_status = Select(driver.find_element_by_id("candidateSearch_status"))
select_status.select_by_value("SHORTLISTED")
print(select_status.options)