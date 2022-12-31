from selenium.webdriver.common.by import By
from pages.BASEPAGE import BasePage

class Dependency_details(BasePage):

    def __init__(self, driver):

        self.driver = driver

    #locators
    Dependents = (By.XPATH,"//div[@role='tab']/following::a[text()='Dependents']")
    add = (By.XPATH,"//h6[text()='Assigned Dependents']/following::button[@type='button']")
    name = (By.XPATH,"//label[text()='Name']/following::input")
    relationship = (By.XPATH,"//label[text()='Relationship']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
    other_relationship = (By.XPATH,"//div[@role='option']//parent::span[text()='Other']")
    pleasespecify = (By.XPATH,"//label[text()='Please Specify']/following::input")
    dateofbirth = (By.XPATH,"//label[text()='Date of Birth']/following::input")
    save = (By.XPATH,"//button[@type='submit']")

    def dependents_click(self):

        return self.driver.find_element(*Dependency_details.Dependents)

    def add_button(self):

        return self.driver.find_element(*Dependency_details.add)

    def name_enter(self):

        return self.driver.find_element(*Dependency_details.name)

    def relation(self):

        return self.driver.find_element(*Dependency_details.relationship)

    def other_relation(self):

        return self.driver.find_element(*Dependency_details.other_relationship)

    def please_specify(self):

        return self.driver.find_element(*Dependency_details.pleasespecify)

    def date_of_birth(self):

        return self.driver.find_element(*Dependency_details.dateofbirth)

    def save_button(self):

        return self.driver.find_element(*Dependency_details.save)







