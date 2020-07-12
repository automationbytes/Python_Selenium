from POMDemo.Locators.locators import Locators

class LoginPage():

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_id = 'txtUsername'
        self.password_textbox_id = 'txtPassword'
        self.login_button_id = 'btnLogin'


    def enterUsername(self,Username):
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")

        self.driver.find_element_by_id(self.username_textbox_id).send_keys(Username)

    def enterPassword(self, Password):
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")#
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(Password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.login_button_id).click()