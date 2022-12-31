from selenium.webdriver.common.by import By
from pages.BASEPAGE import BasePage

class taxexemptionspage(BasePage):

    def __init__(self,driver):

        self.driver = driver

    #locators

    taxexemptions_locator = (By.XPATH,"//a[@class='orangehrm-tabs-item' and text()='Tax Exemptions']")
    status_locator = (By.XPATH,"//label[text()='Status']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
    married_status_locator = (By.XPATH,"//span[text()='Married']//parent::div[@role='option']")
    exemptions_locator = (By.XPATH,"//label[text()='Exemptions']//parent::div//parent::div/div[2]/input[@class='oxd-input oxd-input--active']")
    state_locator = (By.XPATH,"//label[text()='State']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
    state_alaska = (By.XPATH,"//div[@role='option']//parent::span[text()='Alaska']")
    unemployedtstate_locator = (By.XPATH,"//label[text()='Unemployment State']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
    select_unemployedstate_locator = (By.XPATH,"//div[@role='option']//parent::span[text()='Alabama']")
    workstate_locator = (By.XPATH,"//label[text()='Work State']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
    select_workstate = (By.XPATH,"//div[@role='option']//parent::span[text()='Alaska']")
    save_locator = (By.XPATH,"//button[@type='submit']")

    def tax_exemptions(self):

        return self.driver.find_element(*taxexemptionspage.taxexemptions_locator)

    def status(self):

        return self.driver.find_element(*taxexemptionspage.status_locator)

    def married_status(self):

        return self.driver.find_element(*taxexemptionspage.married_status_locator)

    def exemptions(self):

        return self.driver.find_element(*taxexemptionspage.exemptions_locator)

    def state(self):

        return self.driver.find_element(*taxexemptionspage.state_locator)

    def state_selected(self):

        return self.driver.find_element(*taxexemptionspage.state_alaska)

    def unemployedstate(self):

        return self.driver.find_element(*taxexemptionspage.unemployedtstate_locator)

    def select_unemployed(self):

        return self.driver.find_element(*taxexemptionspage.select_unemployedstate_locator)

    def workstate(self):

        return self.driver.find_element(*taxexemptionspage.workstate_locator)

    def selectworkstate(self):

        return self.driver.find_element(*taxexemptionspage.select_workstate)

    def save(self):

        return self.driver.find_element(*taxexemptionspage.save_locator)