from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElement():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length = len(elementListByClassName)
        if elementListByClassName is not None:
            print("Class Name -> Size of the List is: " + str(length))

        elementByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementByTagName)
        if elementByTagName is not None:
            print("Tag Name -> Size of the List is: " + str(length2))


ff = ListOfElement()
ff.test()
