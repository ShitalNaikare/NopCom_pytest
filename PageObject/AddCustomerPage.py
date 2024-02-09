from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerClass:
    Click_CustomerMenu_Xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    Click_Customer_Submenu_Xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    Add_NewCustomer_Xpath = "//a[normalize-space()='Add new']"
    Text_Email_Xpath = "//input[@id='Email']"
    Text_Password_Xpath = "//input[@id='Password']"
    Text_FirstName_Xpath = "//input[@id='FirstName']"
    Text_LastName_Xpath = "//input[@id='LastName']"
    Radio_Male_Xpath = "//label[@for='Gender_Male']"
    Radio_Female_Xpath ="//label[@for='Gender_Female']"
    Calender_Xpath = "//input[@id='DateOfBirth']"
    Text_CompanyName_Xpath = "//input[@id='Company']"
    CheckBox_Tax_Path ="//input[@id='IsTaxExempt']"
    Click_NewsLetter_Xpath ="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/div"
    Click_NewsLetter_List_Xpath = "//li[normalize-space()='Test store 2']"
    DropDown_Manage_Vendor_Xpath = "//select[@id='VendorId']"
    CheckBox_Active_Xpath = "//input[@id='Active']"
    Text_Comment_Xpath = "//textarea[@id='AdminComment']"
    Click_SaveButton_Xpath = "//button[@name='save']"
    Success_Message_Xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self,driver):
        self.driver = driver

    def Click_Customer_Menu(self):
        self.driver.find_element(By.XPATH,self.Click_CustomerMenu_Xpath).click()

    def Click_Customer_Submenu(self):
        self.driver.find_element(By.XPATH,self.Click_Customer_Submenu_Xpath).click()

    def Add_NewCustomer(self):
        self.driver.find_element(By.XPATH,self.Add_NewCustomer_Xpath).click()

    def Enter_Email(self,email):
        self.driver.find_element(By.XPATH,self.Text_Email_Xpath).send_keys(email)
    def Enter_Password(self,password):
        self.driver.find_element(By.XPATH,self.Text_Password_Xpath).send_keys(password)

    def Enter_FirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.Text_FirstName_Xpath).send_keys(firstname)

    def Enter_LastName(self,lastname):
        self.driver.find_element(By.XPATH,self.Text_LastName_Xpath).send_keys(lastname)

    def Select_Gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.Radio_Male_Xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.Radio_Female_Xpath).click()

    def Enter_DOB(self, date):
        self.driver.find_element(By.XPATH, self.Calender_Xpath).send_keys(date)

    def Enter_CompanyName(self, company_name):
        self.driver.find_element(By.XPATH, self.Text_CompanyName_Xpath).send_keys(company_name)

    def CheckBox_Tax(self):
        self.driver.find_element(By.XPATH, self.CheckBox_Tax_Path).click()

    def Click_NewsLetter(self):
        self.driver.find_element(By.XPATH, self.Click_NewsLetter_Xpath ).click()

    def Click_NewsLetter_list(self):
        self.driver.find_element(By.XPATH, self.Click_NewsLetter_List_Xpath).click()

    def DropDown_Manager_of_vendor(self, value):
        Select(self.driver.find_element(By.XPATH, self.DropDown_Manage_Vendor_Xpath)).select_by_visible_text(value)

    def Click_CheckBox_Active(self):
        self.driver.find_element(By.XPATH, self.CheckBox_Active_Xpath).click()

    def Enter_Comment(self, comment):
        self.driver.find_element(By.XPATH, self.Text_Comment_Xpath).send_keys(comment)

    def Click_SaveButton(self):
        self.driver.find_element(By.XPATH, self.Click_SaveButton_Xpath).click()

    def Validate_Success_Message(self):  # pending
        try:
            self.driver.find_element(By.XPATH, self.Success_Message_Xpath)
            return "pass"
        except:
            return "fail"
