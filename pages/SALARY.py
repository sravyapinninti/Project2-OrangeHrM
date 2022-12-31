from selenium.webdriver.common.by import By
from pages.BASEPAGE import BasePage

class salarypage(BasePage):

    def __init__(self,driver):

        self.driver = driver

    #locators

    salary_details = (By.XPATH, "//div[@role='tab']/following::a[text()='Salary']")
    add = (By.XPATH,"//h6[text()='Assigned Salary Components']/following::button[@type='button']")
    salarycomponent_locator = (By.XPATH,"//label[text()='Salary Component']/following::input")
    paygrade_locator = (By.XPATH,"//label[text()='Pay Grade']/following::div/div[text()='-- Select --']")
    grade1_locator = (By.XPATH,"//div[@role='option']/following::span[text()='Grade 1']")
    payfrequency_locator =  (By.XPATH,"//label[text()='Pay Frequency']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
    monthly_pay = (By.XPATH,"//div[@role='option'][4]")
    salarycurrency = (By.XPATH,"//label[text()='Currency']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
    USDsalary = (By.XPATH,"//span[text()='United States Dollar']//parent::div[@role='option']")
    amount_locator = (By.XPATH,"//label[text()='Amount']/following::input")
    toggle_checkbox_locator = (By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    #"//p[text()='Include Direct Deposit Details']//parent::div//parent::div/div/label/input[@type='checkbox']")
    accountnumber_locator = (By.XPATH,"//label[text()='Account Number']/following::input")
    accounttype_locator = (By.XPATH,"//label[text()='Account Type']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
    savingsaccount_locator = (By.XPATH,"//div[@role='option']/following::span[text()='Savings']")
    routing_no_locator = (By.XPATH,"//label[text()='Routing Number']/following::input")
    amount_locator_directdeposit = (By.XPATH,"//label[text()='Amount']/following::input[5]")
    save = (By.XPATH,"//button[text()=' Save ']")

    def salary_button(self):

        return self.driver.find_element(*salarypage.salary_details)

    def add_salary(self):

        return self.driver.find_element(*salarypage.add)

    def salary_component(self):

        return self.driver.find_element(*salarypage.salarycomponent_locator)

    def paygrade(self):

        return self.driver.find_element(*salarypage.paygrade_locator)

    def grade1(self):

        return self.driver.find_element(*salarypage.grade1_locator)

    def payfrequency(self):

        return self.driver.find_element(*salarypage.payfrequency_locator)

    def monthly(self):

        return self.driver.find_element(*salarypage.monthly_pay)

    def salary_currency(self):

        return self.driver.find_element(*salarypage.salarycurrency)

    def USD_salary(self):

        return self.driver.find_element(*salarypage.USDsalary)

    def amount_salary(self):

        return self.driver.find_element(*salarypage.amount_locator)

    def checkbox(self):

        return self.driver.find_element(*salarypage.toggle_checkbox_locator)

    def account_number(self):

        return self.driver.find_element(*salarypage.accountnumber_locator)

    def account_type(self):

        return self.driver.find_element(*salarypage.accounttype_locator)

    def savingsaccount(self):

        return self.driver.find_element(*salarypage.savingsaccount_locator)

    def routing_number(self):

        return self.driver.find_element(*salarypage.routing_no_locator)

    def amount(self):

        return self.driver.find_element(*salarypage.amount_locator_directdeposit)

    def save_button(self):

        return self.driver.find_element(*salarypage.save)



