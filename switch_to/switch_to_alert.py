from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToAlert():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Alert Button
        driver.find_element(By.ID, "name").send_keys("Nery Alert")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)

        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)

        # Confirm Button
        driver.find_element(By.ID, "name").send_keys("Nery Confirm")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)

        alert2 = driver.switch_to.alert
        alert2.dismiss()
        time.sleep(2)

        driver.quit()


ff = SwitchToAlert()
ff.test()