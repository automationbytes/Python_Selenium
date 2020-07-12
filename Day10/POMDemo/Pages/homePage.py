from POMDemo.Locators.locators import Locators
class HomePage():

    def __init__(self,driver):
        self.driver = driver
        self.welcome_link_id = 'welcome'
        self.logout_link_xpath = "//a[text()='Logout']"

    def clickWelcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()