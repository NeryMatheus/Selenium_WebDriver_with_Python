from selenium import webdriver
from selenium.webdriver.common.by import By
from practices.explicit_wait_type1 import ExplicitWaitType1


class ExplicitWaitDemo1():
    def test(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(.5)
        wait = ExplicitWaitType1(driver)

        driver.find_element(By.XPATH, "//a[@href='?pwaLob=wizard-flight-pwa']").click()

        driver.find_element(By.ID, "location-field-leg1-origin-menu").click()
        driver.find_element(By.ID, "location-field-leg1-origin").send_keys("SFO")
        driver.find_element(By.XPATH, "//ul[@class='uitk-typeahead-results no-bullet']//li[1]//button["
                                      "@class='uitk-button uitk-button-medium uitk-button-fullWidth "
                                      "uitk-button-typeahead uitk-type-left has-subtext']").click()

        driver.find_element(By.ID, "location-field-leg1-destination-menu").click()
        driver.find_element(By.ID, "location-field-leg1-destination").send_keys("NYC")
        driver.find_element(By.XPATH, "//div[@class='uitk-menu-container uitk-menu-open uitk-menu-pos-left "
                                      "uitk-menu-container-text-nowrap']//ul[@class='uitk-typeahead-results "
                                      "no-bullet']//li[1]//button[@class='uitk-button uitk-button-medium "
                                      "uitk-button-fullWidth uitk-button-typeahead uitk-type-left "
                                      "has-subtext']").click()

        element = wait.WaitForElement("//button[@data-testid='submit-button']")
        element.click()
        driver.quit()


ff = ExplicitWaitDemo1()
ff.test()
