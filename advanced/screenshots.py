import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Screenshots():
    def test(self):
        baseUrl = "https://courses.letskodeit.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        driver.find_element(By.ID, "email").send_keys("abc@email.com")
        driver.find_element(By.ID, "password").send_keys("abc")
        driver.find_element(By.XPATH, "//input[@class='btn btn-default btn-block btn-md dynamic-button']").click()
        self.takeScreenshot(driver)

    def takeScreenshot(self, driver):
        """
        Take screenshot of the current open web page
        :param driver:
        :return:
        """

        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "C://Users/Mathe/Desktop//Selenium WebDriver with Python 3.x/Advanced/"
        destinationFile = screenshotDirectory + fileName
        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory -> " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue!!")


ff = Screenshots()
ff.test()
