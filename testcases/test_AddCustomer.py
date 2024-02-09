import random
import string

import allure
import pytest
from selenium import webdriver


from PageObject.AddCustomerPage import AddCustomerClass
from PageObject.LoginPage import LoginClass
from Utilities.Logger import LoggenClass
from Utilities.readconfigfile import ReadConfig


class Test_Add_Customer:
    Email = ReadConfig.getEmail()
    Password = ReadConfig.getPassword()
    log = LoggenClass.log_generator()

    @allure.story("Customer")
    @allure.title("Add Customer TestCase")
    @allure.link("https://admin-demo.nopcommerce.com/")
    @allure.severity("Low")
    @pytest.mark.sanity
    def test_addCustomer_003(self, setup):
        self.log.info("Test_case test_addCustomer_003 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        self.lp = LoginClass(self.driver)
        self.log.info("Entering email - " + self.Email)
        self.lp.Enter_Email(self.Email)
        self.log.info("Entering Password - " + self.Password)
        self.lp.Enter_Password(self.Password)
        self.log.info("Click on login button")
        self.lp.Click_LoginButton()
        self.ac = AddCustomerClass(self.driver)
        self.log.info("Click on customer menu")
        self.ac.Click_Customer_Menu()
        self.log.info("Click on customer submenu")
        self.ac.Click_Customer_Submenu()
        self.log.info("Add new customer")
        self.ac.Add_NewCustomer()
        email = Generate_Email()
        self.log.info("Enter email")
        self.ac.Enter_Email(email)
        self.log.info("Enter password")
        self.ac.Enter_Password("Credence@101")
        self.log.info("Enter firstname")
        self.ac.Enter_FirstName("abc")
        self.log.info("Enter Lastname")
        self.ac.Enter_LastName("xyz")
        self.log.info("Select Gender")
        self.ac.Select_Gender("Female")
        self.log.info("Enter date of birth")
        self.ac.Enter_DOB("12/12/2012")
        self.log.info("Enter company name")
        self.ac.Enter_CompanyName("Credence")
        self.log.info("Click on is tax exempt CheckBox")
        self.ac.CheckBox_Tax()
        self.log.info("Click on newsletter")
        self.ac.Click_NewsLetter()
        self.log.info("Click on newsletter list")
        self.ac.Click_NewsLetter_list()
        self.log.info("Select Value for Manager of vendor")
        self.ac.DropDown_Manager_of_vendor("Vendor 1")
        self.log.info("Click on Active Checkbox")
        self.ac.Click_CheckBox_Active()
        self.log.info("Enter Comment")
        self.ac.Enter_Comment("Credence is the best")
        self.log.info("Click Save Button")
        self.ac.Click_SaveButton()
        if self.ac.Validate_Success_Message() == "pass":
            self.log.info("Test_case test_addCustomer_003 is passed")
            self.driver.save_screenshot("..\\Screenshots\\test_addCustomer_003_pass.png")
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\test_addCustomer_003_fail.png")
            self.log.info("Test_case test_addCustomer_003 is Failed")
            assert False

def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase))
    domain = random.choice(["gmail.com","ymail.com","outlook.com"])
    return f"{username}@{domain}"
