# Project2-OrangeHrM

The  project includes "Page Object Model" implementation with "pytest".

Requirements: (i) Python (ii) Pytest (iii) Selenium Python Library (iv) Webdriver for respective Web-browser (v) Web-browser

This project has pages and tests folders

'PAGES' folder includes: 

(i) Admin_Page:
   
The page contains Admin page of the UI.
This page is homepage for the URL.
It contains "searchbox" to search different keywords.

(ii) Basepage:

This page acts as parent page for all pages. Functions created here is used in the test cases and other files.

(iii) Homepage:

This is the homepage of the website.

(iv) Login Page:

This page includes Document Object Model of the test case.
It includes the relative Xpaths of various webelements of the login page of the url.
Using the various Xpaths of webelements of username,password,loginetc..; we create functions for these and are called in testcases.

(v) Dropdown Page:

This page includes  Document Object Model of the test case.
It includes the relative Xpaths of various webelements of the Home page of the url.
Using the various Xpaths of webelements of User Management,Userrole,Adminetc.; we create functions for these and are called in testcases.

(vi) Personal Details Page:

This page includes Document of the test case.
It includes the relative Xpaths of various webelements of the  of the url.
Using the various Xpaths of webelements of all items displayed in side panel and all fields to be given as input in Personal Details page ;
we create functions for these and are called in testcases.

(vii) Contact Details Page:

This page includes Document of the test case.
It includes the relative Xpaths of various webelements of the  of the url.
Using the various Xpaths of webelements of all input fields to be given as input in Contact Details page ;
we create functions for these and are called in testcases.

(viii) Job Details Page:

This page includes Document of the test case.
It includes the relative Xpaths of various webelements of the  of the url.
Using the various Xpaths of webelements of all input fields to be given as input in Job Details page ;
we create functions for these and are called in testcases.

(ix) Depenency Details Page:

This page includes Document of the test case.
It includes the relative Xpaths of various webelements of the  of the url.
Using the various Xpaths of webelements of all input fields to be given as input in Dependency Details page ;
we create functions for these and are called in testcases.

(x) Emergency Contacts :

This page includes Document of the test case.
It includes the relative Xpaths of various webelements of the  of the url.
Using the various Xpaths of webelements of all input fields to be given as input in Emergency Contacts page ;
we create functions for these and are called in testcases.

(xi) Tax Exemptions Page:

This page includes Document of the test case.
It includes the relative Xpaths of various webelements of the  of the url.
Using the various Xpaths of webelements of all input fields to be given as input in Tax Exemptions page ;
we create functions for these and are called in testcases.


'TESTS' FOLDER INCLUDES:

1. Screenshots:

This includes image files of various screenshots from all testscripts from testfile.

2. LogPage:

This page has the log details of the testscript from testfile.

3. HTMLPage:

This page has the HTML details of the testscript from testfile. The HTML details can be viewed in any browser.

4. Testscript(test_orangehrm.py):

This has different 13 test scripts of the project.
Each testscript has different activities to perform.

(a) Test_TC_PIM_01 

This is the first test script of the python file.
1. This launches the URL and login as 'Admin'.
2. Once the URL is launched,then it directs to the Home page.
3. Menu is displayed in the left side of the Home Page.
4. In searchbox, input different menu items in both lower and upper case and validate with menu items in the side panel.

(b) Test_TC_02

1. Validation of Page headers-Dropdown on Home page
2. Once the URL is launched,login using valid credentials and then click on Admin Page.
3. Click on the User Management and move to User and click on Admin-enabled and ESS-disabled.

(c) Test_TC_03

1. This test script includes creation of employee details in PIM module.
2. Employee name,ID and login details of an employee and then save the data.

(d) Test_TC_04

1. Post creation of employee data, Validation of personal details in Pim page is done here.
2. Each input field is checked whether its present or not.

(e) Test_TC_05

1. Login to the website,click on PIM and search with the employee name.
Once all 'Personal details' input field are present, we give input to each field.
2. All text boxes are filled and then clicked on save.
3. Wait till its saved and its reflected in the Employee list Page.

(f) Test_TC_06

1. Login to the website,click on PIM and search with the employee name.
As employee data is already saved,search with the employee name and move to the 'Contact details' of the employee.
2.Fill all the input text boxes of the contact details and then save the data.
3. Wait till the data is saved and reflects on the page.
4. Screenshot is saved so that the user sees that the data is saved .

(g) Test_TC_07

1. Login to the website,click on PIM and search with the employee name.
As employee data is already saved,search with the employee name and move to the 'Emergency Contacts' details of the employee.
2. Fill all the text boxes of the Emergency Contacts by clicling on 'ADD' button.
3. Click on save and wait till the data is saved and then a screenshot file is saved for user to check.

(h) Test_TC_08

1. Login to the website,click on PIM and search with the employee name.
As employee data is already saved,search with the employee name and move to the 'Dependents' details of the employee.
2. There is an ADD button present,click on it and fill all the input fields present.
3. Click 'Save' and wait till its saved and reflects in the page.
4. A 'Screenshot' is clicked and saved for the user to validate.

(i) Test_TC_09

1. Login to the website,click on PIM and search with the employee name.
2. Once the name is found,click on it move to the 'Job Details' of the page.
3. All input fields are filled using 'Send keys','Action Class' etc. and then click on 'Save'.
4. A screenshot is saved for user to validate.

(j) Test_TC_12

1. Login to the website,click on PIM and search with the employee name.
2. Once the name is found,click on it and move to 'Salary' of the UI.
3. Salary Component Details are to be filled and saved.
4. Then click on 'Add' button and fill other tabs as well. Click on 'Save'.
5. A 'Screenshot' is clicked and saved for the user to validate.

(k) Test_TC_13

1. Login to the website,click on PIM and search with the employee name.
2. Once the name is found,click on it and move to 'Tax Exemptions' of the UI.
3. Tax Exemptions Details are to be filled and saved.
4. Toggle Direct Deposit Details and fill all mandatory fields and then click on 'Save'.
5. A 'Screenshot' is clicked and saved for the user to validate.

(l) Test_TC_10_and_TC_11

1. Login to the website,click on PIM and search with the employee name.
2. Once the name is found,click on it and move to 'Job Details' of the UI.
3. In Job Details ,click on Terminate Employment.
4. Reason for termination and various fields are to be filled and click 'Save'.
5. Validate whether its terminated or not by checking with the selected date.
6. Then, 'Activate Employment' is visible,then click on 'Activate Employment' and activate Employee Job.
















