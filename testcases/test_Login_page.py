import time

import allure
import pytest
from selenium import webdriver

from PageObject.LoginPage import LoginClass
from Utilities.Logger import LoggenClass
from Utilities.readconfigfile import ReadConfig


class Test_Login:
    Email = ReadConfig.getEmail()
    Password = ReadConfig.getPassword()
    log = LoggenClass.log_generator()

    @allure.feature('page_title')
    @allure.story('Verifying the page title')
    @allure.issue('ABC-123')
    @allure.link(' https://admin-demo.nopcommerce.com/',name='Orange HRM Website')
    @allure.title('NonCom - Test page_title')
    @allure.description('My test description')
    @allure.link('https://www.example.com')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_Verify_url_001(self,setup):
        self.log.info("Test case test_Verify_url_001 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")

        if self.driver.title == "Your store. Login":
            self.log.info("Test case test_Verify_url_001 is passed")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_Login_002_pass.png")
            assert True
        else:
            self.log.info("Test case test_Verify_url_001 is failed")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_Login_002_fail.png")
            assert False
    @pytest.mark.sanity
    def test_user_Login_002(self,setup):
        self.log.info("Test case test_user_Login_002 is started")
        self.driver = setup
        self.log.info("Opening browser and Navigating to demo_nop_com")
        self.lp = LoginClass(self.driver)
        self.log.info("Enter email-" + self.Email)
        self.lp.Enter_Email(self.Email)
        self.log.info("Enter password-"+ self.Password)
        self.lp.Enter_Password(self.Password)
        self.log.info("Click on login button")
        self.lp.Click_LoginButton()
        time.sleep(5)
        if self.lp.Verify_Login_Status() == "Login pass":
            self.log.info("Test case test_user_Login_002 is passed")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_Login_002_pass.png")
            self.log.info("Click on logout buton")
            self.lp.Click_LogoutButton()
            assert True
        else:
            self.log.info("Test case test_user_Login_002 is failed")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_Login_002_fail.png")
            assert False
        self.log.info("Test case test_user_Login_002 is completed")
