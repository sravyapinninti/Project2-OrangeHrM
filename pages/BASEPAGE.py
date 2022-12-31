import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

#Basepage class is parent of all pages


@pytest.mark.usefixtures("init_driver")
class BasePage:

    def element_presence(self,locator):

        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,locator)))
        self.driver.find_element(By.XPATH,locator)
        return self.driver.find_element(By.XPATH,locator).get_attribute("innerHTML")

    def do_send_keys(self,locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,locator))).send_keys(text)

    def is_displayed(self,locator):
        invalid=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        return invalid.text

    def do_click(self,locator):
        WebDriverWait(self.driver,20).until((EC.element_to_be_clickable(locator))).click()

    def logger(self):

        logger=logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter=logging.Formatter('%(asctime)s : %(levelname)s  : %(name)s : %(message)s ')
        file_handler = logging.FileHandler('orangehrm2.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger






