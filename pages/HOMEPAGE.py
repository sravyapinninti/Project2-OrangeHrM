from pages.BASEPAGE import BasePage
from selenium.webdriver.common.by import By


class Adminpage(BasePage):

   #constructors
    def __init__(self,driver):
        self.driver=driver

    #locators
    search_textbox=(By.XPATH,"//input")

    def search(self):

        return self.driver.find_element(*Adminpage.search_textbox)
