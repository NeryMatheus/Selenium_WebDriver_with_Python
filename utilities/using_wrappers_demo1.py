from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers
import time


class UsingWrappers():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        hw = HandyWrappers(driver)


        textField1 = hw.getElement("name")
        textField1.send_keys("Test's Nery")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.send_keys("12313123")


ff = UsingWrappers()
ff.test()