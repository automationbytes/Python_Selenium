from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@given('the user launches "{url}" url')
def url_launch(context,url):
    context.driver = webdriver.Chrome(executable_path="D:/Webdriver/chromedriver.exe")
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
    context.driver.get("https://www."+url+".com/")

@when('the user is on google homepage')
def goole_homepage(context):
    imagecheck = context.driver.find_element_by_id('hplogo').is_displayed()
    assert imagecheck is True

@then('the user searches "{searchelement}" in searchbox')
def google_searchbar(context,searchelement):
    context.driver.find_element_by_name('q').send_keys(searchelement)

@then('the user clicks enter')
def google_searchbutton(context):
    context.driver.find_element_by_name('q').send_keys(Keys.ENTER)
    print(context.driver.current_window_handle)
    context.driver.quit()


@then('user enter Username as "{user}" and Password as "{pwd}"')
def logincredentials(context,user,pwd):
    context.driver.find_element_by_name('email').send_keys(user)
    context.driver.find_element_by_name('pass').send_keys(pwd)

@then('user clicks on submit')
def fblogin(context):
    #raise NotImplementedError(u'STEP: Then user clicks on submit')
    context.driver.find_element_by_xpath("//input[@aria-label='Log In']").click()


