from selenium import webdriver
from selenium.webdriver.common.by import By

class TestOne():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        radioButtonBMW = driver.find_element_by_id("bmwradio")
        radioButtonBMW.click()

        radioButtonBENZ = driver.find_element_by_id("benzradio")
        radioButtonBENZ.click()

        radioButtonHONDA = driver.find_element_by_id("hondaradio")
        radioButtonHONDA.click()

        selectClass = driver.find_element(By.ID, "carselect")
        selectClass.click()

        #logoByClass = driver.find_element_by_class_name("img-fluid")
        #logoByClass.click()

        #h1Home = driver.find_element_by_tag_name("h1")
        #texto = h1Home.text

        #if texto == "Complete Test Automation Bundle":
         #   print("Tudo certo no h1 do HOME")

ff = TestOne()
ff.test()