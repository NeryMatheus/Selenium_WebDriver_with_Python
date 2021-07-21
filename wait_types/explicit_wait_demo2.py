from selenium import webdriver
from selenium.webdriver.common.by import By
from wait_types.explicit_wait_type import ExplicitWaitType


class ExplicitWaitDemo():
    def test(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)
        driver.implicitly_wait(.5)

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

        # Explicit Wait
        element = wait.waitForElement("//button[@data-testid='submit-button']")
        element.click()
        driver.quit()


ff = ExplicitWaitDemo()
ff.test()
