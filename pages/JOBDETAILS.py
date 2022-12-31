from selenium.webdriver.common.by import By
from pages.BASEPAGE import BasePage


class Job_details(BasePage):

    def __init__(self,driver):

        self.driver = driver

    #locators

    job_details=(By.XPATH,"//a[text()='Job']")
    joineddate = (By.XPATH,"//label[text()='Joined Date']/following::input")
    jobtitle = (By.XPATH,"//label[text()='Job Title']/following::div/div[text()='-- Select --']")
    jobspecification = (By.XPATH,"//label[text()='Job Specification']/following::input")
    jobcategory = (By.XPATH,"//label[text()='Job Category']/following::div/div[text()='-- Select --']")
    subunit = (By.XPATH,"//label[text()='Sub Unit']/following::div/div[text()='-- Select --']")
    location = (By.XPATH,"//label[text()='Location']/following::div/div[text()='-- Select --']")
    employmentstatus = (By.XPATH,"//label[text()='Employment Status']/following::div/div[text()='-- Select --']")
    contractdetails = (By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    contractstartdate = (By.XPATH,"//label[text()='Contract Start Date']/following::input")
    contractenddate = (By.XPATH,"//label[text()='Contract End Date']/following::input")
    save = (By.XPATH,"//button[@type='submit']")
    terminate = (By.XPATH,"//button[text()=' Terminate Employment ']")
    terminationdate = (By.XPATH,"//label[text()='Termination Date']/following::input")
    terminationreason = (By.XPATH,"//label[text()='Termination Reason']/following::div[text()='-- Select --']")
    save_terminate = (By.XPATH,"//p[text()=' * Required']/following::button[text()=' Save ']")
    activate = (By.XPATH,"//h6/following::button[text()=' Activate Employment ']")


    def jobdetails(self):

        return self.driver.find_element(*Job_details.job_details)

    def joined_date(self):

        return self.driver.find_element(*Job_details.joineddate)

    def job_title(self):

        return self.driver.find_element(*Job_details.jobtitle)

    def job_specification(self):

        return self.driver.find_element(*Job_details.jobspecification)

    def job_category(self):

        return self.driver.find_element(*Job_details.jobcategory)

    def sub_unit(self):

        return self.driver.find_element(*Job_details.subunit)

    def location_(self):

        return self.driver.find_element(*Job_details.location)

    def employment_status(self):

        return self.driver.find_element(*Job_details.employmentstatus)

    def contract_details(self):

        return self.driver.find_element(*Job_details.contractdetails)

    def contract_startdate(self):

        return self.driver.find_element(*Job_details.contractstartdate)

    def contract_enddate(self):

        return self.driver.find_element(*Job_details.contractenddate)

    def save_button(self):

        return self.driver.find_element(*Job_details.save)

    def terminate_employment(self):

        return self.driver.find_element(*Job_details.terminate)

    def termination_date(self):

        return self.driver.find_element(*Job_details.terminationdate)

    def termination_reason(self):

        return self.driver.find_element(*Job_details.terminationreason)

    def save_button_terminate(self):

        return self.driver.find_element(*Job_details.save_terminate)

    def activate_employment(self):

        return self.driver.find_element(*Job_details.activate)














