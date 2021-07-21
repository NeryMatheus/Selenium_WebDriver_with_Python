from selenium import webdriver

class ChromeDriverPractice():

    def test(self):
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome()
        # Open the provider URL
        driver.get("https://www.letskodeit.com")


cc = ChromeDriverPractice()
cc.test()
