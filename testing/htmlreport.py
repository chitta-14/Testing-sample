import unittest

import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
#driver=webdriver.Chrome(executable_path="C:\\Users\\CHBUDA\\Desktop\\setupfile\\chromedriver.exe")


# creating an class extracted from unit test
class searchengine(unittest.TestCase):

    # creating user defined methods
    def test_google(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\CHBUDA\\Desktop\\setupfile\\chromedriver.exe")
        self.driver.get("http://www.google.com")
        print("The Title of the page is:" + self.driver.title)
        self.driver.close()

    def test_binge(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\CHBUDA\\Desktop\\setupfile\\chromedriver.exe")
        self.driver.get("https://www.binge.com")
        print("The Title of the page is:" + self.driver.title)
        self.driver.close()


# to run the test methods we need to create main method
if __name__ == "__main__":
    #unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\CHBUDA\\PycharmProjects\\project123\\htmlrepot"))
     unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="C:\\Users\\CHBUDA\\PycharmProjects\\project123\\htmlrepot"))


# to Run go to terminal and type python Tescase1.py
