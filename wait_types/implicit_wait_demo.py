from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWaitDemo():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        loginLink = driver.find_element_by_xpath("//a[@href='/login']")
        loginLink.click()

        emailField = driver.find_element_by_id("email")
        emailField.send_keys("Test GARAIO")


ff = ImplicitWaitDemo()
ff.test()