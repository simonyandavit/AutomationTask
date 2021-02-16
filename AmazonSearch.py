import unittest
from PageObjectModel import *




class MyTestCase(unittest.TestCase):
    def setUp(self):
        model_setup(self)

    def tearDown(self):
        model_tearDown(self)

    def test_dressSearch(self):

        Navigation.searchTherm(self, "dress")

        SearchResults.filterPrice25to50(self)
        SearchResults.clickNthItem(self, SearchResults.findChippestByIndex(self))

        WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.visibility_of_element_located((By.XPATH, XPATH_ADD_CARD_1)))
        self.driver.find_element_by_xpath(XPATH_SELECT_SIZE).click()
        WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.visibility_of_element_located((By.XPATH, XPATH_SMALL_SIZE)))
        self.driver.find_element_by_xpath(XPATH_SMALL_SIZE).click()
        WebDriverWait(self.driver, self.WAIT_DURATION).until_not(EC.visibility_of_element_located((By.XPATH, XPATH_SMALL_SIZE)))

        WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.element_to_be_clickable((By.XPATH, XPATH_ADD_CARD)))
        self.driver.find_element_by_xpath(XPATH_ADD_CARD).click()

        WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.visibility_of_element_located((By.XPATH, XPATH_ADDED)))
        assert(self.driver.find_element_by_xpath(XPATH_ADDED).text == "Added to Cart")



if __name__ == '__main__':
    unittest.main()
