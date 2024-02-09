import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    # browser = request.config.getoption("--browser")
    # if browser == "Chrome":
    #     print("Test run - Browser Chrome")
    #     driver = webdriver.Chrome()
    # elif browser == "Firefox":
    #     print("Test run - Browser Firfox")
    #     driver = webdriver.Firefox()
    # elif browser == "Edge":
    #     print("Test run - Browser Edge")
    #     driver = webdriver.Edge()
    # else:
    #     print("Test run - Browser Headless")
    #     driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(params=[
    ("admin@yourstore.com", "admin", "Pass"),
    ("admin@yourstore.com1", "admin", "Fail"),
    ("admin@yourstore.com", "admin1", "Pass"),
    ("admin@yourstore.com1", "admin1", "Fail")
])
def DataForLogin(request):
    return request.param