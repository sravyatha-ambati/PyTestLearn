import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from DataObjects.greenkart import GreenKart


def test_e2e(browserInstance):
    driver=browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    cart=GreenKart(driver)
    cart.actual_expected()
