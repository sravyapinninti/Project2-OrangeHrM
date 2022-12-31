from pages.BASEPAGE import BasePage
from selenium.webdriver.common.by import By


class Dropdown(BasePage):

   #constructors
    def __init__(self,driver):
        self.driver=driver

    #locators
    admin_tab = (By.XPATH,"//a[@href='/web/index.php/admin/viewAdminModule']")
    user_management = (By.XPATH,"//span[text()='User Management ']")
    user = (By.XPATH,"//a[@href='#']")
    UserRole = (By.XPATH,"//div[@class='oxd-select-text-input']")
    status = (By.XPATH,"//label[text()='Status']/following::div/div")
    admin_userrole = (By.XPATH,"//div[@role='option']/following::span[text()='Admin']")
    enabled = (By.XPATH, "// span[text() = 'Enabled']")
    ESS = (By.XPATH, "//div[@role='option']/following::span[text()='ESS']")
    disabled = (By.XPATH, "// span[text() = 'Disabled']")


    def admin(self):

        return self.driver.find_element(*Dropdown.admin_tab)

    def usermanagement(self):

        return self.driver.find_element(*Dropdown.user_management)

    def user_dropdown(self):

        return self.driver.find_element(*Dropdown.user)

    def user_role(self):

        return self.driver.find_element(*Dropdown.UserRole)

    def status_selection(self):

        return self.driver.find_element(*Dropdown.status)

    def admin_selection(self):

        return self.driver.find_element(*Dropdown.admin_userrole)

    def enabled_status(self):

        return self.driver.find_element(*Dropdown.enabled)

    def ESS_selection(self):

        return self.driver.find_element(*Dropdown.ESS)

    def disabled_status(self):

        return self.driver.find_element(*Dropdown.disabled)

    def disabled_table(self):

        return self.driver.find_element(*Dropdown.disabled).get_attribute("innerHTML")


