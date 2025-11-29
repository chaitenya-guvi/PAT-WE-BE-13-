from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

"""
NOTE : When you call methods for actions on the ActionChains object,
       the actions are stored in a queue in the ActionChains object.
       
       When you call perform(), the events are fired in the order they
       are queued up.


"""



class ActionChainsDragExample:
    url = 'https://qavbox.github.io/demo/dragndrop/'
    driver = webdriver.Chrome()
    # Create the ActionChains Object which will take webdriver as an argument
    action = ActionChains(driver)
    # Locators for draggable and target object
    source_1 = 'draggable'
    target_1 = 'droppable'

    # Browsing Method
    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # ActionChains Drag and Drop
    def drag_drop(self):
        sleep(2)
        source_1_webelement = self.driver.find_element(by=By.ID, value=self.source_1)
        target_1_webelement = self.driver.find_element(by=By.ID, value=self.target_1)

        """ - drag and drop takes a source webelement 
            - and a target webelementt """
        self.action.drag_and_drop(source_1_webelement, target_1_webelement).perform()
        sleep(5)


obj = ActionChainsDragExample()
obj.browsing()
obj.drag_drop()
