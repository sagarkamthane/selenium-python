from selenium.webdriver.common.by import By
from pageobjects.login import Login
from pageobjects.my_account import MyAccount
from pageobjects.profilebutton import ProfileButton


class Homepage:

    signupbutton = (By.CSS_SELECTOR,"a[class = 'social-login']")
    profilebutton = (By.CSS_SELECTOR, "button[class ='action switch']")

    def __init__(self, driver):
        self.driver = driver

    def signup(self):
        self.driver.find_element(*Homepage.signupbutton).click()
        loginpage = Login(self.driver)
        return loginpage

    def profile(self):
        self.driver.find_element(*Homepage.profilebutton).click()
        profilebtn = ProfileButton(self.driver)
        return profilebtn












