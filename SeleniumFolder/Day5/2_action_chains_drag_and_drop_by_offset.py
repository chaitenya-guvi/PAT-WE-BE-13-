from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


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

    # ActionChains Drag and Drop Offset
    def drag_drop_offset(self):
        sleep(2)
        source_1 = self.driver.find_element(by=By.ID, value=self.source_1)
        target_1 = self.driver.find_element(by=By.ID, value=self.target_1)
        # moving horizontally
        # taking element to right side
        self.action.drag_and_drop_by_offset(source_1, xoffset=200, yoffset=0).perform()
        # sleep(5)
        # taking element to left side
        self.action.drag_and_drop_by_offset(source_1, -200, 0).perform()
        # sleep(5)
        # moving vertically
        # taking element downwards
        self.action.drag_and_drop_by_offset(source_1, 0, 50).perform()
        # sleep(5)
        # taking element upwards
        self.action.drag_and_drop_by_offset(source_1, 0, -100).perform()
        # chaining - moving
        sleep(5)
        (self.action.drag_and_drop_by_offset(source_1, xoffset=200, yoffset=0).
         drag_and_drop_by_offset(source_1, -200, 0).
         drag_and_drop_by_offset(source_1, 0, 200).
         drag_and_drop_by_offset(source_1, 0, -200).perform())

obj = ActionChainsDragExample()
obj.browsing()
obj.drag_drop_offset()
