import time

from selenium import webdriver

class GetAttribute():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("type")
        print("Value of attribute is: " + result)

        time.sleep(2)
        driver.quit()

ff = GetAttribute()
ff.test()