import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Example1WebDriverSetupTest(unittest.TestCase):

    def test_driver_manager_chrome(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("https://google.co.th")
        self.assertEqual("Google", driver.title)
        
        driver.implicitly_wait(0.5)
        driver.quit()

    def test_driver_manager_firefox(self):
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

        driver.get("https://google.co.th")
        self.assertEqual("Google", driver.title)

        driver.implicitly_wait(0.5)
        driver.quit()

    # def test_eight_components(self):

    #     # . . . code . . .
    #     service = ChromeService(executable_path=ChromeDriverManager().install())
    #     driver = webdriver.Chrome(service=service)

    #     driver.get("https://google.co.th")

    #     driver.implicitly_wait(0.5)

    #     search_box = driver.find_element_by_name('q')

    #     # search_box = driver.find_element(by=By.NAME, value="q")
    #     search_button = driver.find_element(by=By.NAME, value="btnK")

    #     search_box.send_keys("Selenium")
    #     search_button.click()

    #     search_box = driver.find_element(by=By.NAME, value="q")
    #     self.assertEqual("Selenium", search_box.get_attribute("value"))

    #     username = driver.find_element_by_name('username')
    #     password = driver.find_element_by_name('password')
    #     cont = driver.find_element_by_name('continue')

    #     clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")

    #     login_form = driver.find_element_by_xpath("/html/body/form[1]")       # 1.
    #     login_form = driver.find_element_by_xpath("//form[1]")                # 2.
    #     login_form = driver.find_element_by_xpath("//form[@id='loginForm']")  # 3.

    #     continue_link = driver.find_element_by_link_text('Continue')
    #     continue_link = driver.find_element_by_partial_link_text('Conti')

    #     heading1 = driver.find_element_by_tag_name('h1')

    #     content = driver.find_element_by_class_name('content')

    #     content = driver.find_element_by_css_selector('p.content')

    #     element = driver.find_element_by_tag_name('a')
    #     href = element.get_attribute("href")
    #     enabled = element.is_enabled()
    #     selected = element.is_selected()
    #     displayed = element.is_displayed()

    #     text = element.text

    #     driver.implicitly_wait(0.5)  # seconds

    #     try:
    #         w = WebDriverWait(driver, 10)
    #         w.until(EC.presence_of_element_located((By.ID,'gbw')))
    #     except:
    #         driver.quit()

    #     driver.quit()        

if __name__ == '__main__':
    unittest.main()

