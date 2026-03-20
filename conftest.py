import os
import time
# from utilities.path_creator import PathCreator

import pytest
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
def pytest_addoption(parser):
    parser.addoption(
        "--browsername",
        action="store",
        default="chrome",
        help="browserSelection",

    )

class PathCreator:

    @staticmethod
    def relative_path_creator(file_path):
        base_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_path, file_path)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """This fixture takes screenshot of failed test cases"""
    # Execute the test
    outcome = yield
    result = outcome.get_result()

    # Check if the test has failed
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("browserInstance")  # Access the browser fixture
        if driver:
            timestamp = time.strftime("%Y_%m_%d_%H:%M:%S")
            screenshot_filename = f"{item.name}_{timestamp}.png"
            screenshot_path = PathCreator.relative_path_creator(file_path=f'screenshots/{screenshot_filename}')
            driver.save_screenshot(screenshot_path)
            # driver.get_screenshot_as_file(screenshot_path)
            # screenshot_path="reports/test.png"

@pytest.fixture()
def browserInstance(request):
    browser_name=request.config.getoption("browsername")
    if browser_name== "chrome":
        ser_obj = Service("C:\\Users\\hp\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)
        driver.implicitly_wait(4)
    elif browser_name== "firefox":
        driver=webdriver.Firefox()
        driver.implicitly_wait(4)

    yield driver
    driver.quit()
    #