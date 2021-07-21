#Selecionar ida e volta

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class CalendarSelection():
    def test1(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Clicando no botão de voos
        driver.find_element(By.XPATH, "//a[@href='?pwaLob=wizard-flight-pwa']").click()

        # Cliclando no Departing
        driver.find_element(By.ID, "d1-btn").click()

        departingField = driver.find_element(By.XPATH, "//div[@class='uitk-date-picker-month'][position()=1]//button["
                                                       "@data-day='17']")
        departingField.click()

        time.sleep(3)
        driver.quit()

    def test2(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Clicando no botão de voos
        driver.find_element(By.XPATH, "//a[@href='?pwaLob=wizard-flight-pwa']").click()

        # Cliclando no Departing
        driver.find_element(By.ID, "d1-btn").click()

        calMonth = driver.find_elements(By.XPATH, "//div[@class='uitk-date-picker-month'][position()=1]"
                                                  "//button")

        #time.sleep(3)

        for date in calMonth:
            if date.get_attribute("data-day") == '17':
                date.click()
                break

        #driver.quit()


ff = CalendarSelection()
ff.test2()
