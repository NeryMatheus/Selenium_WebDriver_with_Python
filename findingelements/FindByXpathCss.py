from selenium import webdriver

class FindByXpathCss():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByXpath = driver.find_elements_by_xpath("//input[id='name']")

        if elementByXpath is not None:
            print("We found an element XPATH")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")

        if elementByCss is not None:
            print("We found an element CSS")


ff = FindByXpathCss()
ff.test()