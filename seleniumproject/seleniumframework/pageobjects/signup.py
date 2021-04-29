from selenium.webdriver.common.by import By


class Signup:

    fname = (By.CSS_SELECTOR, "#firstname")
    lname = (By.CSS_SELECTOR, "#lastname")
    email = (By.CSS_SELECTOR, "#email_address_create")
    dob_date = (By.CSS_SELECTOR, "#dob_date")
    anniversary_date = (By.CSS_SELECTOR, "#anniversary_date")
    mobile_number = (By.CSS_SELECTOR, "#mobile_number")
    signinpass = (By.CSS_SELECTOR, "#password-social")
    signinpassconf = (By.CSS_SELECTOR, "#password-confirmation-social")
    signupbtn = (By.CSS_SELECTOR, "button[class = 'action create primary']")

    def __init__(self, driver):
        self.driver = driver

    def f_name(self):
        return self.driver.find_element(*Signup.fname)

    def l_name(self):
        return self.driver.find_element(*Signup.lname)

    def email_id(self):
        return self.driver.find_element(*Signup.email)

    def dob(self):
        return self.driver.find_element(*Signup.dob_date)

    def doa(self):
        return self.driver.find_element(*Signup.anniversary_date)

    def mobile_no(self):
        return self.driver.find_element(*Signup.mobile_number)

    def signin_pass(self):
        return self.driver.find_element(*Signup.signinpass)

    def signin_pass_conf(self):
        return self.driver.find_element(*Signup.signinpassconf)

    def signup_btn(self):
        return self.driver.find_element(*Signup.signupbtn)



