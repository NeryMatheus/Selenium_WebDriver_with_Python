from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToWindow():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switch to window: " + handle)
                driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']//a[@href='/courses']").click()
                searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
                searchBox.send_keys("Python")
                time.sleep(2)
                driver.close()
                break

        # Switch back to the parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Back to the parent handle")
        time.sleep(5)
        driver.quit()


ff = SwitchToWindow()
ff.test()