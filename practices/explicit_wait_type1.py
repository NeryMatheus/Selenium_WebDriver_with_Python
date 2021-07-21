from traceback import print_stack
from practices.handy_wrappers1 import HandyWrappers1

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitType1():
    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers1(driver)

    def WaitForElement(self, locator, locatorType='xpath', timeout=10, poolFrquency=0.5):
        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print("Esperando no máximo :: " + str(timeout) + " segundos pelo elemento clicável!!")
            wait = WebDriverWait(self.driver, 10, poll_frequency=poolFrquency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print("Elemento apareceu na página web")
        except:
            print("Elemento não apareceu na página web")
            print_stack()
        return element
