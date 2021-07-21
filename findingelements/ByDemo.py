from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "name")
        if elementById is not None:
            print("We found an element by ID")

        elementByClassName = driver.find_element(By.CLASS_NAME, "displayed-class")
        if elementByClassName is not None:
            print("We found an element by Class Name")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elementByXpath is not None:
            print("We found an element by XPATH")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "HOME")
        if elementByLinkText is not None:
            print("We found an element by Link Text")



ff = ByDemo()
ff.test()