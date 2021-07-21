from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScrollingElement():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://courses.letskodeit.com/practice")
        driver.implicitly_wait(3)

        # Scroll Down
        driver.execute_script("window.scrollBy(0, 1344);")
        time.sleep(2)

        # Scroll Up
        driver.execute_script("window.scrollBy(0, -1344);")
        time.sleep(2)

        # Scroll Element into view
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -180);")

        # Native a way to scroll element into view
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -1344);")
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))


ff = ScrollingElement()
ff.test()