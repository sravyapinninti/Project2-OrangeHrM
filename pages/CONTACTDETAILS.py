from selenium.webdriver.common.by import By
from pages.BASEPAGE import BasePage


class CONTACT_DETAILS(BasePage):

    def __init__(self,driver):

        self.driver=driver

    #locators

    contactdetails = (By.XPATH,"//a[text()='Contact Details']")
    street1 = (By.XPATH,"//label[text()='Street 1']/following::input")
    street2 = (By.XPATH,"//label[text()='Street 2']/following::input")
    city = (By.XPATH,"//label[text()='City']/following::input")
    state = (By.XPATH,"//label[text()='State/Province']/following::input")
    zip_postalcode = (By.XPATH,"//label[text()='Zip/Postal Code']/following::input")
    country = (By.XPATH,"//div[@class='oxd-select-text-input']")
    telephonehome = (By.XPATH,"//label[text()='Home']/following::input")
    telephonemobile = (By.XPATH,"//label[text()='Mobile']/following::input")
    telephonework = (By.XPATH,"//label[text()='Work']/following::input")
    workEmail = (By.XPATH,"//label[text()='Work Email']/following::input")
    otherEmail = (By.XPATH,"//label[text()='Other Email']/following::input")
    save = (By.XPATH,"//button[text()=' Save ']")

    def contact_details(self):

        return self.driver.find_element(*CONTACT_DETAILS.contactdetails)

    def street_1(self):

        return self.driver.find_element(*CONTACT_DETAILS.street1)

    def street_2(self):

        return self.driver.find_element(*CONTACT_DETAILS.street2)

    def city_enter(self):

        return self.driver.find_element(*CONTACT_DETAILS.city)

    def state_province(self):

        return self.driver.find_element(*CONTACT_DETAILS.state)

    def zippostalcode(self):

        return self.driver.find_element(*CONTACT_DETAILS.zip_postalcode)

    def country_india(self):

        return self.driver.find_element(*CONTACT_DETAILS.country)

    def telephone_home(self):

        return self.driver.find_element(*CONTACT_DETAILS.telephonehome)

    def telephone_mobile(self):

        return self.driver.find_element(*CONTACT_DETAILS.telephonemobile)

    def telephone_work(self):

        return self.driver.find_element(*CONTACT_DETAILS.telephonework)

    def work_email(self):

        return self.driver.find_element(*CONTACT_DETAILS.workEmail)

    def other_email(self):

        return self.driver.find_element(*CONTACT_DETAILS.otherEmail)

    def save_button(self):

        return self.driver.find_element(*CONTACT_DETAILS.save)














