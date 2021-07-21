from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class Sliders():
    def test(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Mudando para o frame do slider
        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 80, 0).perform()
            print("Sliding Element Successful")
            time.sleep(2)

        except:
            print("Sliding failed on element")


ff = Sliders()
ff.test()