from selenium.webdriver.common.by import By


class ProfileButton:

    myaccbtn = (By.LINK_TEXT, 'My Account')
    wishlistbtn = (By.CSS_SELECTOR, "li[class = 'link wishlist']")
    signoutbtn = (By.CSS_SELECTOR, 'li[class="authorization-link"]')

    def __init__(self, driver):
        self.driver =driver

    def my_acc_button(self):
        return self.driver.find_element(*ProfileButton.myaccbtn).click()

    def wishlist_button(self):
        return self.driver.find_element(*ProfileButton.wishlistbtn).click()

    def signout_button(self):
        return self.driver.find_element(*ProfileButton.signoutbtn).click()




