import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class calculateGrade_ATS(unittest.TestCase):

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
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"course-list\"]/table/tbody/tr/td[1]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"add-courses\"]/a/button").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/div[1]/input")
        elem.send_keys("Selenium Test")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/div[2]/input")
        elem.send_keys("100")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/div[3]/input")
        elem.send_keys("95")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/div[4]/input")
        elem.send_keys("04/20/2020")
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        assert "Assignment Created"
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/course_summary/1/course_summary_assignment")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"assignment-table\"]/a/button").click()
        time.sleep(1)
        assert "Grade Calculated"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()