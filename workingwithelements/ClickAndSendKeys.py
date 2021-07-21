from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='header5']//a[@href='/login']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID, "password")
        passwordField.send_keys("123123")

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys("test")


ff = ClickAndSendKeys()
ff.test()