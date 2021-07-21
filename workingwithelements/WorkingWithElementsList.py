from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():
    def testListOfElements(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        radioButtonsList = driver.find_elements(
            By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        sizeList = len(radioButtonsList)
        print("Size of the List: " + str(sizeList))

        for radioBtn in radioButtonsList:
            isSelected = radioBtn.is_selected()

            if not isSelected:
                radioBtn.click()
                time.sleep(2)


ff = WorkingWithElementsList()
ff.testListOfElements()