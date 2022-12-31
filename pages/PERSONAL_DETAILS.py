from selenium.webdriver.common.by import By
from pages.BASEPAGE import BasePage


class PERSONAL_DETAILS(BasePage):

    def __init__(self,driver):

        self.driver=driver

    #locators

    personaldetails=(By.XPATH,"//a[text()='Personal Details']")
    nickname = (By.XPATH,"//label[text()='Nickname']/following::div[1]/input")
    otherid = (By.XPATH,"//label[text()='Other Id']/following::div/input")
    driverslicenseno = (By.XPATH,"//label[text()='Driver's License Number']/following::div/input")
    licenseexpirydate = (By.XPATH,"//label[text()='License Expiry Date']/following::div/input")
    SSNnumber = (By.XPATH,"//label[text()='SSN Number']/following::div/input")
    SINNumber = (By.XPATH,"//label[text()='SIN Number']/following::div/input")
    Nationality = (By.XPATH,"//label[text()='Nationality']/following::i")
    indian = (By.XPATH,"//div[@role='option']/following::span[text()='Indian']")
    maritalstatus = (By.XPATH,"//label[text()='Marital Status']/following::div/div/div/i")
    single = (By.XPATH,"//div[@role='option']/following::span[text()='Single']")
    dateofbirth = (By.XPATH,"//label[text()='Date of Birth']/following::div/div/input")
    gender = (By.XPATH,"//label[text()='Gender']/following::span")
    militaryservice = (By.XPATH,"//label[text()='Military Service']/following::input")
    savebutton = (By.XPATH,"//button[@type='submit']")
    Bloodtype = (By.XPATH,"//label[text()='Blood Type']/following::div/div/div/div")
    bloodgroup = (By.XPATH,"//div[@role='option']/following::span[text()='A+']")
    save = (By.XPATH,"//div[@class='oxd-form-actions']/following::button[text()=' Save ']")

    def personal_details_employee(self):

        return self.driver.find_element(*PERSONAL_DETAILS.personaldetails)

    def nick_name(self):

        return self.driver.find_element(*PERSONAL_DETAILS.nickname)

    def other_id(self):

        return self.driver.find_element(*PERSONAL_DETAILS.otherid)

    def Dl(self):

        return self.driver.find_element(*PERSONAL_DETAILS.driverslicenseno)

    def license_expiry_date(self):

        return self.driver.find_element(*PERSONAL_DETAILS.licenseexpirydate)

    def SSN_number(self):

        return self.driver.find_element(*PERSONAL_DETAILS.SSNnumber)

    def SIN_Number(self):

        return self.driver.find_element(*PERSONAL_DETAILS.SINNumber)

    def Nationality_select(self):

        return self.driver.find_element(*PERSONAL_DETAILS.Nationality)

    def indian_nationality(self):

        return self.driver.find_element(*PERSONAL_DETAILS.indian)

    def marital_status(self):

        return self.driver.find_element(*PERSONAL_DETAILS.maritalstatus)

    def single_maritalstatus(self):

        return self.driver.find_element(*PERSONAL_DETAILS.single)

    def date_of_birth(self):

        return self.driver.find_element(*PERSONAL_DETAILS.dateofbirth)

    def gender_male(self):

        return self.driver.find_element(*PERSONAL_DETAILS.gender)

    def military_service(self):

        return self.driver.find_element(*PERSONAL_DETAILS.militaryservice)

    def save_button(self):

        return self.driver.find_element(*PERSONAL_DETAILS.savebutton)

    def blood_type(self):

        return self.driver.find_element(*PERSONAL_DETAILS.Bloodtype)

    def bloodgroup_robert(self):

        return self.driver.find_element(*PERSONAL_DETAILS.bloodgroup)

    def save_click(self):

        return self.driver.find_element(*PERSONAL_DETAILS.save)







