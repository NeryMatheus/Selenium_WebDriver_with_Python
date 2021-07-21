from selenium import webdriver

class ElementState():

    def isEnable(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_class_name("gLFyf")
        e1State = e1.is_enabled() # True for enabled and False for disabled
        print("E1 is Enabled? -> " + str(e1State))
        e1.send_keys("Matheus Nery")


eff = ElementState()
eff.isEnable()