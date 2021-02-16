from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Selectors import *

def model_setup(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.amazon.com/")
    self.WAIT_DURATION = 4

def model_tearDown(self):
    self.driver.quit()

class Navigation():
    def searchTherm(self, term):
        elem_search = self.driver.find_element_by_xpath(XPATH_SEARCH)
        elem_search.clear()
        elem_search.send_keys(term)
        elem_search.submit()

class SearchResults():
    def filterPrice25to50(self):
        self.driver.find_element_by_xpath(XPATH_PRICE_FILTER).click()
        WebDriverWait(self.driver,self.WAIT_DURATION).until(EC.visibility_of_element_located((By.XPATH, XPATH_ANY_PRICE)))

    def findChippestByIndex(self):
        elems_price = self.driver.find_elements_by_xpath(XPATH_PRICE_WHOLE)
        e_priceWhole = self.driver.find_elements_by_xpath(XPATH_PRICE_WHOLE)
        e_priceFraction = self.driver.find_elements_by_xpath(XPATH_PRICE_FRACTION)

        min = float(e_priceWhole[0].text + "." + e_priceFraction[0].text)
        chipest_index = 0
        for i in range(1,len(e_priceWhole)):
            if float(e_priceWhole[i].text + "." + e_priceFraction[i].text) < min:
                min = float(e_priceWhole[i].text + "." + e_priceFraction[i].text)
                chipest_index = i
        return chipest_index

    def clickNthItem(self,n):
        e_items = self.driver.find_elements_by_xpath(XPATH_ITEM_LINK)
        e_items[n].click()



