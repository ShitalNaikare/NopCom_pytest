import allure
import pytest
from selenium import webdriver

from PageObject.LoginPage import LoginClass
from Utilities.Logger import LoggenClass
from Utilities.readconfigfile import ReadConfig
from allure_commons.types import AttachmentType

class Test_Login_params:

    log = LoggenClass.log_generator()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_user_Login_params_004(self,setup,DataForLogin):
        self.log.info("Test case test_user_Login_002 is started")
        self.driver = setup
        self.log.info("Opening browser and Navigating to demo_nop_com")
        self.lp = LoginClass(self.driver)
        self.log.info("Enter email-" + DataForLogin[0])
        self.lp.Enter_Email(DataForLogin[0])
        self.log.info("Enter password-"+ DataForLogin[1])
        self.lp.Enter_Password(DataForLogin[1])
        self.log.info("Click on login button")
        self.lp.Click_LoginButton()
        TestCase_status_List = []
        if self.lp.Verify_Login_Status() == "Login pass":
            self.log.info("Login pass")
            if DataForLogin[2] == "pass":
                self.log.info("Expected pass")
                self.log.info("Taking Screenshot")
                allure.attach(self.driver.get_screenshot_as_png(),name="test_user_Login_002_pass",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshots\\test_user_Login_params_004_pass.png")
                TestCase_status_List.append("pass")
            elif DataForLogin[2] == "fail":
                self.log.info("Expected fail")
                self.log.info("Taking screenshots")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_user_Login_002_fail",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshots\\test_user_Login_params_004_fail.png")
                TestCase_status_List.append("fail")
                self.lp.Click_LogoutButton()
        elif self.lp.Verify_Login_Status() == "Login fail":
            self.log.info("Login fail")
            if DataForLogin[2] == "pass":
                self.log.info("Expected pass")
                self.log.info("Taking screenshots")
                allure.attach(self.driver.get_screenshot_as_png(),name="test_user_Login_002_fail",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshots\\test_user_Login_params_004_fail.png")
                TestCase_status_List.append("fail")
            elif DataForLogin[2] == "fail":
                self.log.info("Expected fail")
                TestCase_status_List.append("pass")
                self.log.info("Taking screenshots")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_user_Login_002_pass",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshots\\test_user_Login_params_004_pass.png")
        print(TestCase_status_List)
        if "fail" in TestCase_status_List:
            self.log.info("Test_case test_user_login_params_004 is Failed")
            assert False
        else:
            self.log.info("Test_case test_user_login_params_004 is Passed")
            assert True
        self.log.info("Test_case test_user_login_params_004 is Completed")




