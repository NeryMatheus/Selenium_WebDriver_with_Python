import time

from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = "https://www.goibibo.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(5)

partialText = "Del"
textToSelect = "Deline, Canada(YWJ)"

textElement = driver.find_element(By.ID, "gosuggest_inputSrc")
textElement.send_keys(partialText)

ulElement = driver.find_element(By.ID, "react-autosuggest-1")
inner_html = ulElement.get_attribute("innerHTML")
#print(inner_html)

liELement = driver.find_elements(By.TAG_NAME, "li")

for element in liELement:
    if textToSelect in element.text:
        element.click()
        break

time.sleep(5)

driver.quit()