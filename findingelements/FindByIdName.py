from selenium import webdriver


class FindByIdName():
    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found an element by Id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("We found an element by Name")


ff = FindByIdName()
ff.test()
