from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class DragAndDrop():
    def test(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Acessando o frame dentro da página web do Jquery
        driver.switch_to.frame(0)

        # Encontrando o elemento que será arrastado(drag) e o que receberá()drop
        fromElement = driver.find_element(By.ID, "draggable")
        toElement = driver.find_element(By.ID, "droppable")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(fromElement, toElement).perform()
            # actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag and Drop Element Successful")
            time.sleep(2)

        except:
            print("Drag and Drop failed on element")


ff = DragAndDrop()
ff.test()

