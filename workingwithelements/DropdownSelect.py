from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class DropdownSelect():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value!!")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honza by index!!")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")


ff = DropdownSelect()
ff.test()