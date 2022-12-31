from selenium.webdriver.common.by import By
from pages.BASEPAGE import BasePage


class Emergency_contacts(BasePage):

    def __init__(self,driver):

        self.driver = driver

    emergencycontacts = (By.XPATH,"//div[@role='tab']/following::a[text()='Emergency Contacts']")
    add = (By.XPATH,"//h6[text()='Assigned Emergency Contacts']/following::button[@type='button']")
    name_contact = (By.XPATH,"//label[text()='Name']/following::div/input")
    relationship = (By.XPATH,"//label[text()='Relationship']/following::div/input")
    Hometelephone = (By.XPATH,"//label[text()='Home Telephone']/following::div/input")
    mobile = (By.XPATH,"//label[text()='Mobile']/following::div/input")
    worktelephone = (By.XPATH,"//label[text()='Work Telephone']/following::div/input")
    save = (By.XPATH,"//button[text()=' Save ']")

    def emergency_contacts(self):

        return self.driver.find_element(*Emergency_contacts.emergencycontacts)

    def add_emergency_contacts(self):

        return self.driver.find_element(*Emergency_contacts.add)

    def name_emergency_contacts(self):

        return self.driver.find_element(*Emergency_contacts.name_contact)

    def relationship_emergency_contacts(self):

        return self.driver.find_element(*Emergency_contacts.relationship)

    def home_telephone(self):

        return self.driver.find_element(*Emergency_contacts.Hometelephone)

    def mobile_no(self):

        return self.driver.find_element(*Emergency_contacts.mobile)

    def work_telephone(self):

        return self.driver.find_element(*Emergency_contacts.worktelephone)

    def save_button(self):

        return self.driver.find_element(*Emergency_contacts.save)







