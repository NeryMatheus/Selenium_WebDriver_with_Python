# Selenium_WebDriver_with_Python

## Assuntos abordados:

  #### Encontrar elementos tanto pelo id, quanto por Seletores CSS ou pelo XPATH

      Xpath{
         //div[@id='header5']  
         //div[@id='header5']//ul//li//a
         //img[@class='img-fluid']

         //div[@class='zen-removable']//input[2]
         //div[@id='header5']//a[text()='ALL COURSES']
         //div[@id='header5']//a[contains(@class,'dynamic-link') and contains(@href,'courses')]

         //a[@href='/courses']//parent::li
         //a[@href='/courses']//parent::li//preceding-sibling::li
         //a[@href='/courses']//parent::li//preceding-sibling::li//following-sibling::li
         //table[@id='product']//parent::td[text()='Python Programming Language ']//following-sibling::td
         //div[@id='layout']//div[text()='The Green Mile']//following-sibling::div[1]
         //table[@id='product']//td[text()='Python Programming Language ']//following-sibling::td
      }
##
  #### Trabalhando com elementos web
##
  #### Xpath dinâmico
##
  #### Implicit Wait e Explict Wait
##
  #### Advanced
      {
         //div[@class='uitk-date-picker-month'][position()=1]//button[@data-day='22']
         Calendar Selection
         ScreenShot 
         Scrolling Elements
         Auto Complete
         Window size
      }
##
  #### Switch to 
    {
        switch to window
        switch to frame
        switch to alert
    }
##
  #### Working with action class
    {
        Ambos os casos que será executado necessita-se da biblioteca ActionChains
        Mouse hover actions
        Drag and drop element on a web page
        Slider
    }
##
  #### Logging Infrastructure
##
  #### Teste Unitário - Unittest