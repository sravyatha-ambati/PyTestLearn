import time

from selenium.webdriver.common.by import By


class GreenKart:
    def __init__(self,driver):
        self.driver=driver
        self.input_search=(By.CSS_SELECTOR, "input[type='search']")
        self.product_list=(By.XPATH, "//div[@class='products']/div/h4")

    def actual_expected(self):
        self.driver.find_element(self.input_search).send_keys("ot")
        time.sleep(2)
        actualList = []
        Productname = self.driver.find_elements()
        for productnames in Productname:
            actualList.append(productnames.text)

        print(actualList)
        expectedList = ['Beetroot - 1 Kg', 'Carrot - 1 Kg', 'Potato - 1 Kg']

        assert actualList == expectedList
        print("Comparing etween merge conflicts")

        # print(Productname)