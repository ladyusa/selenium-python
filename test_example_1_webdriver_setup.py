import unittest
from selenium import webdriver

class Example1WebDriverSetupTest(unittest.TestCase):

    def test_driver_manager_chrome(self):
        driver = webdriver.Chrome() 

        driver.get("https://google.co.th")
        self.assertEqual("Google", driver.title)
        
        driver.quit()

    def test_driver_manager_firefox(self):
        driver = webdriver.Firefox()

        driver.get("https://google.co.th")
        self.assertEqual("Google", driver.title)

        driver.quit()

if __name__ == '__main__':
    unittest.main()

