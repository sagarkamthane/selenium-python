from selenium.webdriver.common.by import By

from pageobjects.signup import Signup


class Login:

    loginpass = (By.CSS_SELECTOR, "#pass")
    loginbtn = (By.CSS_SELECTOR, "button[type = 'button']")
    newacc = (By.CSS_SELECTOR, "a[class = 'action create']")


    def __init__(self, driver):
        self.driver = driver

    def user_login(self, id):
        name = (By.CSS_SELECTOR, "#email")
        id_input = self.driver.find_element(*name).send_keys(id)
        return id_input

    def password(self):
        return self.driver.find_element(*Login.loginpass)

    def login_button(self):
        return self.driver.find_element(*Login.loginbtn)

    def new_acc(self):
        self.driver.find_element(*Login.newacc).click()
        signup = Signup(self.driver)
        return signup


