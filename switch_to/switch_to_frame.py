from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using ID
        # driver.switch_to.frame("courses-iframe")

        # Switch to frame using name
        # driver.switch_to.frame("iframe-name")

        # Switch to frame using numbers
        driver.switch_to.frame(0)

        time.sleep(2)
        # Search Course
        searchBox_iFrame = driver.find_element(By.XPATH, "//input[@id='search']")
        searchBox_iFrame.send_keys("Python")
        time.sleep(2)

        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        driver.find_element(By.ID, "name").send_keys("Switch to frame test successful")
        time.sleep(2)

        driver.quit()


ff = SwitchToFrame()
ff.test()