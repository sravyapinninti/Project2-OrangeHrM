import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["edge"],scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        web_driver.get(url)

        web_driver.maximize_window()
        web_driver.implicitly_wait(20)
        request.cls.driver = web_driver

        yield

        web_driver.close()

    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        web_driver.get(url)

        web_driver.maximize_window()
        web_driver.implicitly_wait(10)
        request.cls.driver = web_driver

        yield

        web_driver.close()

    if request.param == "edge":
        web_driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        web_driver.get(url)

        web_driver.maximize_window()
        web_driver.implicitly_wait(14)

        request.cls.driver = web_driver

        yield

        web_driver.close()



