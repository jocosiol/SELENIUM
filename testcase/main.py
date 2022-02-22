import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("Setup")
        self.driver = webdriver.Chrome("/Users/javiercosio/Documents/UPWORD/SELENIUM/chromedriver")
        self.driver.get("https://www.python.org")

    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()