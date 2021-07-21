from selenium import webdriver

class IEDriverPractice():
    def test(self):
        # Instantiate the IE Browser Command
        driver = webdriver.Ie()
        # Open the  provided URL
        driver.get("https://www.letskodeit.com")


ieObject = IEDriverPractice()
ieObject.test()