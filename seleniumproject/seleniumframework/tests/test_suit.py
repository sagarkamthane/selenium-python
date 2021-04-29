import time
from selenium import webdriver
import pytest
from pageobjects.homepage import Homepage
from pageobjects.login import Login
from pageobjects.signup import Signup
from testdata.testdata import HomePageTestData
from utilities.baseclass import BaseClass


class TestCases(BaseClass):
    def test_e2e(self, setup, test_data):
        log = self.logger()
        home = Homepage(self.driver)
        self.wait("a[class = 'social-login']")
        loginpage = home.signup()
        self.wait("a[class = 'action create']")
        loginpage.user_login(test_data["id"])
        loginpage.password().send_keys(test_data["pass"])
        loginpage.login_button().click()
        log.info(f'user logged in with id:{test_data["id"]} and pass:{test_data["pass"]}')

        self.wait('button[class ="action switch"]')
        profilebtn = home.profile()
        profilebtn.my_acc_button()
        log.info("user went to my account")

    @pytest.fixture(params=HomePageTestData.get_test_data("testcase1"))
    def test_data(self, request):
        return request.param









        











