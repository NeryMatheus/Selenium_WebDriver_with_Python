from selenium import webdriver

class BrowserInteractions():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()

        # Window Maximize
        driver.maximize_window()

        # Open the Url
        driver.get(baseUrl)

        # Get Title
        title = driver.title
        print("Title of the web page is: " + title)

        # Get Current URL
        currentUrl = driver.current_url
        print("Current URL of the web page is: " + currentUrl)

        # Browser Refresh
        driver.refresh()
        print("Browser refresh 1st time!!")
        driver.get(driver.current_url)
        print("Browser refresh 2st time!!")

        # Open another URL
        driver.get("https://courses.letskodeit.com/login")
        currentUrl = driver.current_url
        print("Current URL of the web page is: " + currentUrl)

        # Browser Back
        driver.back()
        print("Go one step back in browser history!! ")
        currentUrl = driver.current_url
        print("Current URL of the web page is: " + currentUrl)

        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history!!!")
        currentUrl = driver.current_url
        print("Current URL of the web page is: " + currentUrl)

        # Get page source
        # pageSource = driver.page_source
        # print("page Source: " + pageSource)

        # Browser Close/Quit
        # driver.close()
        driver.quit()


ff = BrowserInteractions()
ff.test()