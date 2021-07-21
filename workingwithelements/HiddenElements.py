import time

from selenium import webdriver

class HiddenElements():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Find the State of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_selected() # True if visible, False if hidden, Excpetion if not present in the DOM
        print("Text is visible? -> " + str(textBoxState))
        time.sleep(2)

        # Click the Hide Button
        hiddenBtn = driver.find_element_by_id("hide-textbox")
        hiddenBtn.click()
        time.sleep(2)

        # Find the State of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text box is visible? " + str(textBoxState))
        time.sleep(2)

        # Click the Show Button
        showBtn = driver.find_element_by_id("show-textbox")
        showBtn.click()
        time.sleep(2)

        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? -> " + str(textBoxState))
        time.sleep(2)

        # Browser Close
        driver.quit()

    def testExpedia(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        driver.find_element_by_xpath("//ul[@id='uitk-tabs-button-container']//a[contains(@href,"
                                     "'?pwaLob=wizard-flight-pwa')]").click()
        time.sleep(2)

        driver.find_element_by_xpath("//ul[@id='uitk-tabs-button-container']//div[@id='adaptive-menu']").click()
        time.sleep(2)

        driver.find_element_by_xpath("//div[@class='uitk-flex uitk-flex-align-items-center "
                                     "uitk-flex-justify-content-space-between uitk-step-input childStepInput "
                                     "uitk-step-input-mounted']//input["
                                     "@id='child-input-0']//following-sibling::button").click()
        time.sleep(2)

        driver.find_element_by_xpath("//select[@id='child-age-input-0-0']//option[@value='10']").click()
        time.sleep(2)

ff = HiddenElements()
#ff.test()
ff.testExpedia()