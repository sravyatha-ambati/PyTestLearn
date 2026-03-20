import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:\\Users\\hp\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys("ot")
time.sleep(2)
actualList=[]
Productname=driver.find_elements(By.XPATH,"//div[@class='products']/div/h4")
for productnames in Productname:
    actualList.append(productnames.text)

print(actualList)
expectedList=['Beetroot - 1 Kg','Carrot - 1 Kg','Potato - 1 Kg']

assert actualList== expectedList

# print(Productname)