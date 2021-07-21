from selenium import webdriver

class FindByLinkText():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_link_text("HOME")

        if elementByLinkText is not None:
            print("We found an element By Link Text")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("SUP")

        if elementByPartialLinkText is not None:
            print("We found an element by Partial Link Text")


ff = FindByLinkText()
ff.test()