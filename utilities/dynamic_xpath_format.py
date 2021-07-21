from selenium import webdriver
from selenium.webdriver.common.by import By


class DynamicXpathFormat():
    def test(self):
        baseUrl = "https://courses.letskodeit.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Login -> Lecture: "How to click and type on a web element"
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        email = driver.find_element(By.ID, "email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "password")
        password.send_keys("abcabc")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Search for courses -> You don't need to search the course
        # You can select it without searching also
        #searchBox = driver.find_element(By.ID, "search")
        #searchBox.click()
        #searchBox.send_keys("Javascript")

        # Select Course
        _course = "//h4[contains(@class,'dynamic-heading') and contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()


ff = DynamicXpathFormat()
ff.test()
