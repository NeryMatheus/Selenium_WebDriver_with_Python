from selenium import webdriver


class RunFFTests():
    def testMethod(self):
        # Instantiate the FF Browser Command
        driver = webdriver.Firefox()
        # Open the provider URL
        driver.get("https://www.letskodeit.com")


ff = RunFFTests()
ff.testMethod()