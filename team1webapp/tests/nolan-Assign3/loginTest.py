import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class login_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "neitzen"
        pwd = "isqa3900"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/form/div[1]/input")
        elem.send_keys(user)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/form/div[2]/input")
        elem.send_keys(pwd)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()