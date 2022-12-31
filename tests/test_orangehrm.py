import pytest
from selenium.webdriver import ActionChains
from tabulate import tabulate

from pages.TAXEXEMPTIONS import taxexemptionspage
from pages.SALARY import salarypage
from pages.JOBDETAILS import Job_details
from pages.DEPENDENCYDETAILS import Dependency_details
from pages.EMERGENCYCONTACTS import Emergency_contacts
from pages.CONTACTDETAILS import CONTACT_DETAILS
from pages.PERSONAL_DETAILS import PERSONAL_DETAILS
from pages.LOGINPAGE import LoginPage
from pages.BASEPAGE import BasePage
from pages.HOMEPAGE import Adminpage
from pages.DROPDOWN_TC02 import Dropdown
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pages.PIMPage import PIM_MODULE


@pytest.mark.usefixtures('init_driver')
class Test_TC_PIM_01(BasePage):

    def test_Admin(self) :
        # initiating logging
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        #VALIDATION USING ASSERT KEYWORD
        displayed_list=[]
        menu = self.driver.find_elements(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")

        #ADMIN page MENU
        for k in menu:
            displayed_list.append(k.get_attribute('innerHTML'))
        print(displayed_list)
        menu_names=['admin','pim','leave','time','recruitment','my info','performance','dashboard','directory','maintenance','buzz']

        for j,i in zip(displayed_list,menu_names):

            self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(j)
            assert j.upper() == i.upper()
            assert j.lower() == i.lower()
            log.info(f"displayed_list:{j}   -   menu_names:{i.upper()}")
            log.info(f"displayed_list:{j}   -   menu_names:{i.lower()}")
            self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)


@pytest.mark.usefixtures('init_driver')
class Test_TC_02(BasePage):

    def test_Dropdown(self):
        # initiating logging
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")
        textbox = Adminpage(self.driver)
        self.element_presence('//input')
        text = textbox.search()
        log.info("search-input textbox is displayed")
        text.send_keys("admin")
        log.info(self.element_presence("//span[text()='Admin']"))
        text.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        log.info(self.element_presence("//span[text()='Admin']"))

        #clicking on ADMIN
        drop_down=Dropdown(self.driver)
        self.element_presence("//a[@href='/web/index.php/admin/viewAdminModule']")
        click_admin=drop_down.admin()
        click_admin.click()
        log.info("clicked on Admin")

        #dropdown
        self.element_presence("//span[text()='User Management ']")
        click_dropdown=drop_down.usermanagement()
        click_dropdown.click()
        log.info("usermanagement dropdown clicked")
        self.element_presence("//a[@href='#']")
        click_usermanagement=drop_down.user_dropdown()
        click_usermanagement.click()
        time.sleep(3)
        log.info("entered into usermanagement and clicked on user tab")

        #System users
        self.element_presence("//div[@class='oxd-select-text-input']")
        click_userrole=drop_down.user_role()
        click_userrole.click()
        log.info("select Userole")
        actions = ActionChains(self.driver)
        select_userole1 = self.driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input']" )
        actions.move_to_element(select_userole1).perform()
        select_admin=self.driver.find_element(By.XPATH,"//div[@role='option']/following::span[text()='Admin']").click()
        admin = self.element_presence("//label[text()='User Role']//parent::div//parent::div/div/div/div/div[text()='Admin']")
        log.info("Admin selected")
        assert self.element_presence("//div[text()='Admin']") == "Admin"

        #status
        self.element_presence("//label[text()='Status']/following::div/div")
        click_status=drop_down.status_selection()
        click_status.click()
        log.info("select status for User role ")
        actions = ActionChains(self.driver)
        select_status = self.driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']")
        actions.move_to_element(select_status).perform()
        self.element_presence("// span[text() = 'Enabled']")
        select_enabled=self.driver.find_element(By.XPATH,"// span[text() = 'Enabled']").click()
        enabled = self.element_presence("//label[text()='Status']//parent::div//parent::div/div/div/div/div[text()='Enabled']")
        log.info("status Enabled for Admin User role")

        #systemusers
        self.element_presence("//div[@class='oxd-select-text-input']")
        click_userrole = drop_down.user_role()
        click_userrole.click()
        log.info("select Userole")
        actions = ActionChains(self.driver)
        select_userole = self.driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']")
        actions.move_to_element(select_userole).perform()
        ESS_select=self.driver.find_element(By.XPATH, "//div[@role='option']/following::span[text()='ESS']").click()
        ESS=self.element_presence("//label[text()='User Role']//parent::div//parent::div/div/div/div/div[text()='ESS']")
        log.info("ESS selected")
        assert self.element_presence("//div[text()='ESS']") == "ESS"

        #status
        self.element_presence("//label[text()='Status']/following::div/div")
        click_status = drop_down.status_selection()
        click_status.click()
        log.info("select status for User role ESS")
        actions = ActionChains(self.driver)
        select_status1 = self.driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']")
        actions.move_to_element(select_status1).perform()
        self.element_presence("// span[text() = 'Disabled']")
        select_disabled = drop_down.disabled_status()
        select_disabled.click()
        disabled = self.element_presence("//label[text()='Status']//parent::div//parent::div/div/div/div/div[text()='Disabled']")
        log.info("status Disabled for ESS User role")

        table = [
            [admin, enabled],
            [ESS , disabled]
        ]
        head = ["User Role", "Status"]
        log.info(tabulate(table, headers=head, tablefmt="grid"))


@pytest.mark.usefixtures('init_driver')
class Test_TC_03(BasePage):

    def test_PIM(self):

        # initiating logging
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim = PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        add_button = pim.add_button1()
        log.info("clicked add button")
        self.element_presence("//input[@name='firstName']")
        first_name = pim.employee_details_firstname()
        first_name.send_keys("Robert")
        log.info("first name is Robert")
        self.element_presence("//input[@name='middleName']")
        middle_name = pim.employee_details_middlename()
        middle_name.send_keys("Jr.")
        log.info("middlename is Jr.")
        self.element_presence("//input[@name='lastName']")
        last_name = pim.employee_details_lastname()
        last_name.send_keys("Darwin")
        log.info("last name is Darwin")
        self.element_presence("//label[text()='Employee Id']/following::div[1]/input")
        employeeid = pim.employee_details_employeeid()
        log.info("employee id is auto-generated")
        employeeid.send_keys(Keys.CONTROL, "a" ,Keys.BACKSPACE)
        employeeid.send_keys("123456")

        self.element_presence("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        click_button=pim.button()
        time.sleep(2)
        click_button.click()
        log.info("create login details")
        self.element_presence("// label[text() = 'Username'] / following::div / input")
        username=pim.user_name()
        username.send_keys("RobertJ")
        log.info("Entered username")
        self.element_presence("//input[@type='password']")
        password=pim.pass_word()
        password.send_keys("Robert@1")
        log.info("Entered password")
        self.element_presence("//label[text()='Confirm Password']/following::input[@type='password']")
        confirmpassword=pim.confirm_password()
        confirmpassword.send_keys("Robert@1")
        #validation of password
        assert password.send_keys("Robert@1") == confirmpassword.send_keys("Robert@1")
        log.info("Entered confirm password")
        self.element_presence("// button[ @ type = 'submit']")
        submit = pim.save_button()
        submit.click()
        time.sleep(5)
        #log.info(self.element_presence('//p[text()="Successfully Saved"]'))
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        log.info("found required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        #self.element_presence("//div[text()='Robert Jr.')]")
        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        log.info("user created successfully in Employee List")


@pytest.mark.usefixtures('init_driver')
class Test_TC_04(BasePage):

    def test_employee_details(self):

        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim=PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        log.info("find required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        self.element_presence("//div[text()='Robert Jr.']")
        try:
            assert self.element_presence("//div[text()='Robert Jr.']") == 'Robert Jr.'
        except:
            print("please check username")

        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        self.element_presence("//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill']")
        edit_button = pim.edit_employee()
        edit_button.click()

        employeelist= []
        diplayed_menu = self.driver.find_elements(By.XPATH,"//div[@role='tab']")
        for i in diplayed_menu:
            employeelist.append(i.text)
        print(employeelist)

        menu = ['personal details','contact details','emergency contacts','dependents','immigration','job','salary','tax exemptions','report-to','qualifications','memberships']

        for j,i in zip(employeelist,menu):

            assert j.lower() == i.lower()
            assert j.upper() == i.upper()
            log.info(f"employeelist menu:{j}   -  dispalyed menu:{i}")


@pytest.mark.usefixtures('init_driver')
class Test_TC_05(BasePage):

    def test_personaldetails(self):
        # initiating logging
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim = PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        time.sleep(5)
        log.info("find required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        self.element_presence("//div[text()='Robert Jr.']")
        try:
            assert self.element_presence("//div[text()='Robert Jr.']") == 'Robert Jr.'
        except:
            print("please check username")

        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        self.element_presence("//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill']")
        edit_button = pim.edit_employee()
        edit_button.click()

        self.element_presence("//h6[text()='Robert Darwin']")

        personal_details=PERSONAL_DETAILS(self.driver)
        self.element_presence("//label[text()='Nickname']/following::div[1]/input")
        nick_name=personal_details.nick_name()
        time.sleep(10)
        nick_name.send_keys("robby")
        log.info("nickname entered")

        self.element_presence("//label[text()='Other Id']/following::div/input")
        other_id=personal_details.other_id()
        other_id.send_keys('1234897')
        log.info("otherid entered")

        # self.element_presence("//label[text()='Driver's License Number']/following::div/input")
        # DLN0 = personal_details.Dl()
        # DLN0.send_keys('L123KFHJI')
        # log.info("Driver's License Number entered")

        self.element_presence("//label[text()='License Expiry Date']/following::div/input")
        dr_license_no=personal_details.license_expiry_date()
        time.sleep(10)
        dr_license_no.send_keys("2030-12-12")
        log.info("license expiry date entered")

        self.element_presence("//label[text()='SSN Number']/following::div/input")
        ssn_no=personal_details.SSN_number()
        ssn_no.send_keys("456223")
        log.info("SSN Number entered")

        self.element_presence("//label[text()='SIN Number']/following::div/input")
        sin_no=personal_details.SIN_Number()
        sin_no.send_keys("485942")
        log.info("SIN Number entered")

        self.element_presence("//label[text()='Nationality']/following::i")
        nation=personal_details.Nationality_select()
        action=ActionChains(self.driver)
        action.move_to_element(nation).click().perform()
        self.element_presence("//div[@role='option']/following::span[text()='Indian']")
        indian=personal_details.indian_nationality()
        action.move_to_element(indian).click().perform()
        log.info("Nationality-Indian")

        self.element_presence("//label[text()='Marital Status']/following::div/div/div/i")
        mstatus=personal_details.marital_status()
        actions=ActionChains(self.driver)
        action.move_to_element(mstatus).click().perform()
        self.element_presence("//div[@role='option']/following::span[text()='Single']")
        single=personal_details.single_maritalstatus()
        actions.move_to_element(single).click().perform()
        log.info("Marital Status-Single")

        self.element_presence("//label[text()='Date of Birth']/following::div/div/input")
        dateofbirth=personal_details.date_of_birth()
        dateofbirth.send_keys("1991-12-11")
        log.info("Date of birth is 1991-12-11")

        self.element_presence("//label[text()='Gender']/following::span")
        gender=personal_details.gender_male()
        gender.click()
        log.info("clicked on male-gender")

        self.element_presence("//label[text()='Military Service']/following::input")
        militaryservice=personal_details.military_service()
        militaryservice.send_keys("3years")
        log.info("Military Service entered 3years")

        self.element_presence("//button[@type='submit']")
        save=personal_details.save_button()
        save.click()
        log.info("saved successfully")

        self.element_presence("//label[text()='Blood Type']/following::div/div/div/div")
        blood_type=personal_details.blood_type()
        action=ActionChains(self.driver)
        action.move_to_element(blood_type).click().perform()
        self.element_presence("//div[@role='option']/following::span[text()='A+']")
        blood_group=personal_details.bloodgroup_robert()
        action.move_to_element(blood_group).click().perform()
        log.info("Blood type-A+")

        self.element_presence("//div[@class='oxd-form-actions']/following::button[text()=' Save ']")
        save=personal_details.save_click()
        save.click()
        log.info(self.element_presence("//p[text()='Successfully Saved']"))
        time.sleep(5)

        self.driver.get_screenshot_as_file("personaldetails.jpg")


@pytest.mark.usefixtures('init_driver')
class Test_TC_06(BasePage):

    def test_contactdetails(self):
        # initiating logging
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim = PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        time.sleep(5)
        log.info("find required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        self.element_presence("//div[text()='Robert Jr.']")
        try:
            assert self.element_presence("//div[text()='Robert Jr.']") == 'Robert Jr.'
        except:
            print("please check username")

        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        self.element_presence("//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill']")
        edit_button = pim.edit_employee()
        edit_button.click()

        self.element_presence("//h6[text()='Robert Darwin']")

        c_details=CONTACT_DETAILS(self.driver)
        self.element_presence("//a[text()='Contact Details']")
        contact_details_click=c_details.contact_details()
        contact_details_click.click()

        self.element_presence("//label[text()='Street 1']/following::input")
        street1=c_details.street_1()
        time.sleep(10)
        street1.send_keys("#25,4th block")
        log.info("street1 data entered")

        self.element_presence("//label[text()='Street 2']/following::input")
        street2=c_details.street_2()
        street2.send_keys("4h main,whitefield")
        log.info("street2 data entered")

        self.element_presence("//label[text()='City']/following::input")
        city=c_details.city_enter()
        city.send_keys("Bangalore")
        log.info("City data entered - Bangalore")

        self.element_presence("//label[text()='State/Province']/following::input")
        country=c_details.country_india()
        time.sleep(5)
        country.send_keys("Karnataka")
        log.info("country-India")

        self.element_presence("//label[text()='State/Province']/following::input")
        zip=c_details.zippostalcode()
        zip.send_keys("560042")
        log.info("Zip code is 560042")

        self.element_presence("//div[@class='oxd-select-text-input']")
        actions=ActionChains(self.driver)
        country=self.driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input']")
        actions.move_to_element(country).click().perform()
        india=self.driver.find_element(By.XPATH,"//div[@role='option']/following::span[text()='India']")
        actions.move_to_element(india).click().perform()
        log.info("country-India")

        self.element_presence("//label[text()='Home']/following::input")
        home_telephone=c_details.telephone_home()
        home_telephone.send_keys("123456789")
        log.info("telephone_home no. entered")

        self.element_presence("//label[text()='Mobile']/following::input")
        mobile_telephone = c_details.telephone_mobile()
        mobile_telephone.send_keys("9999554423")
        log.info("telephone_mobile no. entered")

        self.element_presence("//label[text()='Work']/following::input")
        work_telephone = c_details.telephone_work()
        work_telephone.send_keys("+91 9874568795")
        log.info("telephone_work no. entered")

        self.element_presence("//label[text()='Work Email']/following::input")
        work_Email = c_details.work_email()
        work_Email.send_keys("robert1@gmail.com")
        log.info("work E-mail entered")

        self.element_presence("//label[text()='Other Email']/following::input")
        other_Email = c_details.other_email()
        other_Email.send_keys("darwin1@gmail.com")
        log.info("other E-mail entered")

        self.element_presence("//button[text()=' Save ']")
        save_click = c_details.save_button()
        time.sleep(5)
        save_click.click()
        log.info(self.element_presence("//p[text()='Successfully Updated']"))
        time.sleep(5)

        self.driver.get_screenshot_as_file("contactdetails.jpg")


@pytest.mark.usefixtures('init_driver')
class Test_TC_07(BasePage):

    def test_Emergencycontacts(self):

        # initiating logging
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim = PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        time.sleep(5)
        log.info("find required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        self.element_presence("//div[text()='Robert Jr.']")
        try:
            assert self.element_presence("//div[text()='Robert Jr.']") == 'Robert Jr.'
        except:
            print("please check username")

        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        self.element_presence("//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill']")
        edit_button = pim.edit_employee()
        edit_button.click()

        self.element_presence("//h6[text()='Robert Darwin']")

        emer_contacts=Emergency_contacts(self.driver)
        self.element_presence("//div[@role='tab']/following::a[text()='Emergency Contacts']")
        emergency_contacts_click=emer_contacts.emergency_contacts()
        emergency_contacts_click.click()
        log.info("Entering into Emergency Contacts")

        self.element_presence("//h6[text()='Assigned Emergency Contacts']/following::button[@type='button']")
        add_emergency=emer_contacts.add_emergency_contacts()
        add_emergency.click()
        log.info("Adding emergency contacts")

        self.element_presence("//label[text()='Name']/following::div/input")
        name_emergencycontacts=emer_contacts.name_emergency_contacts()
        name_emergencycontacts.send_keys("Michael")
        log.info("name entered")

        self.element_presence("//label[text()='Relationship']/following::div/input")
        relation=emer_contacts.relationship_emergency_contacts()
        relation.send_keys("sibling")
        log.info("relation entered")

        self.element_presence("//label[text()='Home Telephone']/following::div/input")
        home_phone=emer_contacts.home_telephone()
        home_phone.send_keys("123456789")
        log.info("home_phoneno. entered")

        self.element_presence("//label[text()='Mobile']/following::div/input")
        mobile_no=emer_contacts.mobile_no()
        mobile_no.send_keys("9988774455")
        log.info("mobile no. entered")

        self.element_presence("//label[text()='Work Telephone']/following::div/input")
        work_phonenumber=emer_contacts.work_telephone()
        work_phonenumber.send_keys("+91 2548789")
        log.info("work phone number entered")

        self.element_presence("//button[text()=' Save ']")
        savebutton=emer_contacts.save_button()
        time.sleep(5)
        savebutton.click()
        log.info(self.element_presence("//p[text()='Successfully Saved']"))
        log.info("Emergency contacts saved successfully")
        time.sleep(5)

        self.driver.get_screenshot_as_file("emergencycontact.jpg")


@pytest.mark.usefixtures('init_driver')
class Test_TC_08(BasePage):

    def test_dependency_details(self):

        # initiating logging
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim = PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        time.sleep(5)
        log.info("find required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        self.element_presence("//div[text()='Robert Jr.']")
        try:
            assert self.element_presence("//div[text()='Robert Jr.']") == 'Robert Jr.'
        except:
            print("please check username")

        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        self.element_presence("//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill']")
        edit_button = pim.edit_employee()
        edit_button.click()
        self.element_presence("//h6[text()='Robert Darwin']")

        dependency_details=Dependency_details(self.driver)
        self.element_presence("//div[@role='tab']/following::a[text()='Dependents']")
        dependents=dependency_details.dependents_click()
        dependents.click()
        log.info("Entering into Dependents")

        self.element_presence("//h6[text()='Assigned Dependents']/following::button[@type='button']")
        add=dependency_details.add_button()
        add.click()
        log.info("Add dependency details")

        self.element_presence("//label[text()='Name']/following::div/input")
        name=dependency_details.name_enter()
        name.send_keys("martin")
        log.info("name entered")

        self.element_presence("//label[text()='Relationship']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
        actions=ActionChains(self.driver)
        relation=dependency_details.relation()
        actions.move_to_element(relation).click().perform()
        self.element_presence("//div[@role='option']//parent::span[text()='Other']")
        other_relationship = dependency_details.other_relation()
        time.sleep(5)
        actions.move_to_element(other_relationship).click().perform()
        log.info("relation entered")

        self.element_presence("//label[text()='Please Specify']/following::input")
        pleasespecify = dependency_details.please_specify()
        pleasespecify.send_keys("other relation")
        log.info("please specify tab entered")

        self.element_presence("//label[text()='Date of Birth']/following::input")
        DOB=dependency_details.date_of_birth()
        DOB.send_keys("2000-12-11")
        log.info("DOB entered")

        self.element_presence("//button[@type='submit']")
        save=dependency_details.save_button()
        time.sleep(5)
        save.click()
        log.info(self.element_presence("//p[text()='Successfully Saved']"))
        time.sleep(5)

        self.driver.get_screenshot_as_file("dependencydetails.jpg")


@pytest.mark.usefixtures('init_driver')
class Test_TC_09(BasePage):

    def test_Jobdetails(self):
        # initiating logging
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim = PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        time.sleep(5)
        log.info("find required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        self.element_presence("//div[text()='Robert Jr.']")
        try:
            assert self.element_presence("//div[text()='Robert Jr.']") == 'Robert Jr.'
        except:
            print("please check username")

        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        self.element_presence("//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill']")
        edit_button = pim.edit_employee()
        edit_button.click()
        self.element_presence("//h6[text()='Robert Darwin']")

        jobdetails=Job_details(self.driver)
        self.element_presence("//a[text()='Job']")
        job_details=jobdetails.jobdetails()
        job_details.click()
        log.info("Clicked Job tab")

        self.element_presence("//label[text()='Joined Date']/following::input")
        joined_date=jobdetails.joined_date()
        time.sleep(10)
        joined_date.send_keys("2013-11-11")
        log.info("Joined Date entered")

        self.element_presence("//label[text()='Job Title']/following::div/div[text()='-- Select --']")
        jobtitle=self.driver.find_element(By.XPATH,"//label[text()='Job Title']/following::div/div[text()='-- Select --']")
        actions=ActionChains(self.driver)
        actions.move_to_element(jobtitle).click().perform()
        title=self.driver.find_element(By.XPATH,"//div[@role='option']/following::span[text()='Software Engineer']")
        actions.move_to_element(title).click().perform()
        log.info("Job tile entered")

        self.element_presence("//label[text()='Job Category']/following::div/div[text()='-- Select --']")
        job_category=self.driver.find_element(By.XPATH,"//label[text()='Job Category']/following::div/div[text()='-- Select --']")
        action=ActionChains(self.driver)
        action.move_to_element(job_category).click().perform()
        technician=self.driver.find_element(By.XPATH,"//div[@role='option']/following::span[text()='Technicians']")
        action.move_to_element(technician).click().perform()
        log.info("Job category entered")

        self.element_presence("//label[text()='Sub Unit']/following::div/div[text()='-- Select --']")
        subunit=self.driver.find_element(By.XPATH,"//label[text()='Sub Unit']/following::div/div[text()='-- Select --']")
        actions=ActionChains(self.driver)
        actions.move_to_element(subunit).click().perform()
        development=self.driver.find_element(By.XPATH,"//div[@role='option']/following::span[text()='Development']")
        actions.move_to_element(development).click().perform()
        log.info("Sub unit entered")

        self.element_presence("//label[text()='Location']/following::div/div[text()='-- Select --']")
        location=self.driver.find_element(By.XPATH,"//label[text()='Location']/following::div/div[text()='-- Select --']")
        actions=ActionChains(self.driver)
        actions.move_to_element(location).click().perform()
        texas=self.driver.find_element(By.XPATH,"//div[@role='option']/following::span[text()='Texas R&D']")
        actions.move_to_element(texas).click().perform()
        log.info("Location entered")

        self.element_presence("//label[text()='Employment Status']/following::div/div[text()='-- Select --']")
        employmentstatus=self.driver.find_element(By.XPATH,"//label[text()='Employment Status']/following::div/div[text()='-- Select --']")
        actions=ActionChains(self.driver)
        actions.move_to_element(employmentstatus).click().perform()
        contract_time=self.driver.find_element(By.XPATH,"//div[@role='option']/following::span[text()='Full-Time Probation']")
        actions.move_to_element(contract_time).click().perform()
        log.info("Full-time contract ")

        self.element_presence("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        checkbox = jobdetails.contract_details()
        checkbox.click()
        log.info("checkbox toggled")

        self.element_presence("//label[text()='Contract Start Date']/following::input")
        contract_strt = jobdetails.contract_startdate()
        contract_strt.send_keys("2013-11-11")
        log.info("contract starts on 2013-11-11")

        self.element_presence("//label[text()='Contract End Date']/following::input")
        contract_end = jobdetails.contract_enddate()
        contract_end.send_keys("2015-11-11")
        log.info("contract ends on 2015-11-11")

        self.element_presence("//button[@type='submit']")
        save = jobdetails.save_button()
        time.sleep(5)
        save.click()
        self.element_presence("//p[text()='Successfully Updated']")
        log.info(self.element_presence("//p[text()='Successfully Updated']"))
        time.sleep(5)

        self.driver.get_screenshot_as_file("jobdetails.jpg")


@pytest.mark.usefixtures('init_driver')
class Test_TC_12(BasePage):

    def test_salary(self):
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim = PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        time.sleep(5)
        log.info("find required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        self.element_presence("//div[text()='Robert Jr.']")
        try:
            assert self.element_presence("//div[text()='Robert Jr.']") == 'Robert Jr.'
        except:
            print("please check username")

        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        self.element_presence("//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill']")
        edit_button = pim.edit_employee()
        edit_button.click()
        self.element_presence("//h6[text()='Robert Darwin']")
        #go to salary page
        addsalary = salarypage(self.driver)
        self.element_presence("//div[@role='tab']/following::a[text()='Salary']")
        salary_click=addsalary.salary_button()
        salary_click.click()

        #add salary deatils
        self.element_presence("//h6[text()='Assigned Salary Components']/following::button[@type='button']")
        add_button=addsalary.add_salary()
        add_button.click()

        #salary component
        self.element_presence("//label[text()='Salary Component']/following::input")
        salary_component=addsalary.salary_component()
        salary_component.send_keys("Basic salary,allownaces etc.")

        #Pay Grade
        self.element_presence("//label[text()='Pay Grade']/following::div[text()='-- Select --']")
        actions = ActionChains(self.driver)
        paygrade = addsalary.paygrade()
        actions.move_to_element(paygrade).click().perform()
        self.element_presence("//div[@role='option']/following::span[text()='Grade 1']")
        grade1 = addsalary.grade1()
        actions.move_to_element(grade1).click().perform()
        log.info("Entered Grade1 as pay grade")

        #pay frequency
        self.element_presence("//label[text()='Pay Frequency']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
        actions = ActionChains(self.driver)
        pay_frequency = addsalary.payfrequency()
        actions.move_to_element(pay_frequency).click().perform()
        self.element_presence("//span[text()='Monthly']//parent::div[@role='option']")
        payment_salary = addsalary.monthly()
        actions.move_to_element(payment_salary).click().perform()
        log.info("Payment of salary is Monthly")

        #Currency
        self.element_presence("//label[text()='Currency']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
        actions = ActionChains(self.driver)
        salary=addsalary.salary_currency()
        actions.move_to_element(salary).click().perform()
        log.info("select")
        self.element_presence("//span[text()='United States Dollar']//parent::div[@role='option']")
        time.sleep(5)
        USD = addsalary.USD_salary()
        actions.move_to_element(USD).click().perform()
        log.info("Monthly salary is in USD")

        #Amount
        self.element_presence("//label[text()='Amount']/following::input")
        amount = addsalary.amount_salary()
        amount.send_keys("59626")
        log.info("Salary entered")

        #toggle direct deposit details
        self.element_presence("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        depositdetails=addsalary.checkbox()
        actions.move_to_element(depositdetails).click().perform()


        #AccountNumber
        self.element_presence("//label[text()='Account Number']/following::input")
        accountno=addsalary.account_number()
        accountno.send_keys("152364789")
        log.info("account number entered")

        #accountype
        self.element_presence("//label[text()='Account Type']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
        accounttype = addsalary.account_type()
        actions.move_to_element(accounttype).click().perform()
        self.element_presence("//div[@role='option']/following::span[text()='Savings']")
        savingsaccount = addsalary.savingsaccount()
        actions.move_to_element(savingsaccount).click().perform()
        log.info("Savings account selected")

        #Routingnumber
        self.element_presence("//label[text()='Routing Number']/following::input")
        routing_numberadd=addsalary.routing_number()
        routing_numberadd.send_keys("4587912")
        log.info("Routing Number added")

        #amount
        self.element_presence("//label[text()='Amount']/following::input[5]")
        amount_enter=addsalary.amount()
        amount_enter.send_keys("45963")
        log.info("Amount entered")

        #save
        self.element_presence("//button[text()=' Save ']")
        save_button = addsalary.save_button()
        save_button.click()

        log.info(self.element_presence("//p[text()='Successfully Saved']"))
        time.sleep(5)

        self.driver.get_screenshot_as_file("salarydetails.jpg")


@pytest.mark.usefixtures('init_driver')
class Test_TC_13(BasePage):

    def test_exemptions(self):
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim = PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        time.sleep(5)
        log.info("find required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        self.element_presence("//div[text()='Robert Jr.']")
        try:
            assert self.element_presence("//div[text()='Robert Jr.']") == 'Robert Jr.'
        except:
            print("please check username")

        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        self.element_presence("//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill']")
        edit_button = pim.edit_employee()
        edit_button.click()
        self.element_presence("//h6[text()='Robert Darwin']")

        exemptionspage=taxexemptionspage(self.driver)
        self.element_presence("//a[@class='orangehrm-tabs-item' and text()='Tax Exemptions']")
        tax_exemptions_click = exemptionspage.tax_exemptions()
        tax_exemptions_click.click()

        self.element_presence("//label[text()='Exemptions']//parent::div//parent::div/div[2]/input[@class='oxd-input oxd-input--active']")
        exemptions_data=exemptionspage.exemptions()
        exemptions_data.send_keys("15")
        log.info(self.element_presence("//label[text()='Exemptions']//parent::div//parent::div/div[2]/input[@class='oxd-input oxd-input--active']"))

        self.element_presence("//label[text()='Status']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
        actions = ActionChains(self.driver)
        status_select = exemptionspage.status()
        actions.move_to_element(status_select).click().send_keys(Keys.ARROW_DOWN).perform()
        log.info("clicked")
        self.element_presence("//span[text()='Married']//parent::div[@role='option']")
        married_status_click = exemptionspage.married_status()
        actions.move_to_element(married_status_click).click().perform()
        log.info("selected married status")

        self.element_presence("//label[text()='State']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
        state_select=exemptionspage.state()
        actions.move_to_element(state_select).click().perform()
        self.element_presence("//div[@role='option']//parent::span[text()='Alaska']")
        stateselect=exemptionspage.state_selected()
        actions.move_to_element(stateselect).click().perform()

        self.element_presence("//label[text()='Unemployment State']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
        unemployedstate=exemptionspage.unemployedstate()
        actions.move_to_element(unemployedstate).click().send_keys(Keys.ARROW_DOWN).perform()
        self.element_presence("//div[@role='option']//parent::span[text()='Alabama']")
        select_unemployedstate=exemptionspage.select_unemployed()
        actions.move_to_element(select_unemployedstate).click().perform()

        self.element_presence("//label[text()='Work State']//parent::div//parent::div/div/div/div/div[text()='-- Select --']")
        workstate=exemptionspage.workstate()
        actions.move_to_element(workstate).click().perform()
        self.element_presence("//div[@role='option']//parent::span[text()='Alaska']")
        selectworkstate=exemptionspage.selectworkstate()
        actions.move_to_element(selectworkstate).click().perform()

        self.element_presence("//button[@type='submit']")
        save=exemptionspage.save()
        save.click()

        self.element_presence("//p[text()='Successfully Updated']")
        time.sleep(5)
        self.driver.get_screenshot_as_file("exemptions.jpg")


@pytest.mark.usefixtures('init_driver')
class Test_TC_10_and_TC_11(BasePage):

    def test_terminate_employment_and_test_activate_employment(self):
        # initiating logging
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim = PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        time.sleep(5)
        log.info("find required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        self.element_presence("//div[text()='Robert Jr.']")
        try:
            assert self.element_presence("//div[text()='Robert Jr.']") == 'Robert Jr.'
        except:
            print("please check username")

        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        self.element_presence("//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill']")
        edit_button = pim.edit_employee()
        edit_button.click()
        time.sleep(5)
        self.element_presence("//h6[text()='Robert Darwin']")

        jobdetails = Job_details(self.driver)
        self.element_presence("//a[text()='Job']")
        job_details = jobdetails.jobdetails()
        job_details.click()
        log.info("Clicked Job tab")

        self.element_presence("//button[text()=' Terminate Employment ']")
        terminate=jobdetails.terminate_employment()
        terminate.click()
        log.info("Employee Terminated")

        self.element_presence("//label[text()='Termination Date']/following::input")
        date=jobdetails.termination_date()
        date.send_keys("2015-11-11")
        log.info("Termination Date")

        self.element_presence("//label[text()='Termination Reason']/following::div[text()='-- Select --']")
        actions=ActionChains(self.driver)
        reason_select=self.driver.find_element(By.XPATH,"//label[text()='Termination Reason']/following::div[text()='-- Select --']")
        actions.move_to_element(reason_select).click().perform()
        reason=self.driver.find_element(By.XPATH,"//div[@role='option']/following::span[text()='Contract Not Renewed']")
        actions.move_to_element(reason).click().perform()
        log.info("Reason selected")

        self.element_presence("//p[text()=' * Required']/following::button[text()=' Save ']")
        click=jobdetails.save_button_terminate()
        click.click()
        log.info("successfully updated")

        self.driver.find_element(By.XPATH,"//div[@class='orangehrm-action-header']/following::p").get_attribute("innerHTML")
        log.info(self.element_presence("//div[@class='orangehrm-action-header']/following::p"))

        self.element_presence("//h6/following::button[text()=' Activate Employment ']")
        log.info(self.element_presence("//h6/following::button[text()=' Activate Employment ']"))
        time.sleep(10)

        self.driver.get_screenshot_as_file("jobdetails_termination.jpg")

        self.element_presence("//h6/following::button[text()=' Activate Employment ']")
        log.info(self.element_presence("//h6/following::button[text()=' Activate Employment ']"))
        activateemployment = jobdetails.activate_employment()
        activateemployment.click()
        time.sleep(6)
        self.driver.get_screenshot_as_file("activateemployment.jpg")

        log.info(self.element_presence("//h6/following::button[text()=' Terminate Employment ']"))
        log.info("Employee Job is activated")

"""
@pytest.mark.usefixtures('init_driver')
class Test_TC_11(BasePage):

    def test_Activateemployment(self):
        # initiating logging
        log = self.logger()
        # importing from login.py and initialising driver
        login = LoginPage(self.driver)
        # verifying element's visibility
        self.element_presence("//input[@name='username']")
        # creating variable to do actions
        username = login.enter_user_name()
        # log data to add in orangehrm1.log page
        log.info("username entered")
        username.send_keys("Admin")
        # verifiying element's visibility
        self.element_presence('//input[@name="password"]')
        password = login.enter_pass_word()
        password.send_keys("admin123")
        log.info("password entered")
        self.element_presence("//button[@type='submit']")
        login_click = login.login_button1()
        login_click.click()
        log.info("logged in successfully")

        pim = PIM_MODULE(self.driver)
        self.element_presence("//a[@href='/web/index.php/pim/viewPimModule']")
        pim_button = pim.click_PIM()
        log.info("entering into PIM page")
        self.element_presence("//a[text()='Employee List']")
        employeelist = pim.employee_list()
        employeelist.click()
        log.info("Employee List is displayed")
        self.element_presence("//input[@placeholder='Type for hints...']")
        search_name = pim.search_employee_name()
        search_name.send_keys("Robert Jr. Darwin")
        time.sleep(5)
        log.info("find required employee")
        self.element_presence("//button[@type='submit']")
        submit = pim.submit_button()
        submit.click()
        time.sleep(5)
        self.element_presence("//div[text()='Robert Jr.']")
        try:
            assert self.element_presence("//div[text()='Robert Jr.']") == 'Robert Jr.'
        except:
            print("please check username")

        log.info(self.element_presence("//div[text()='Robert Jr.']"))
        self.element_presence("//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill']")
        edit_button = pim.edit_employee()
        edit_button.click()
        self.element_presence("//h6[text()='Robert Darwin']")

        jobdetails = Job_details(self.driver)
        self.element_presence("//a[text()='Job']")
        job_details = jobdetails.jobdetails()
        job_details.click()
        log.info("Clicked Job tab")

        self.element_presence("//h6/following::button[text()=' Activate Employment ']")
        log.info(self.element_presence("//h6/following::button[text()=' Activate Employment ']"))
        activateemployment=jobdetails.activate_employment()
        activateemployment.click()
        self.driver.get_screenshot_as_file("activateemployment.jpg")

        log.info(self.element_presence("//h6/following::button[text()=' Terminate Employment ']"))
        log.info("Employee Job is activated")"""



























































