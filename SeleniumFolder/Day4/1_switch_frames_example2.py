import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class HerokuIframePractice:

    def __init__(self):
        self.url = "https://the-internet.herokuapp.com/nested_frames"
        self.driver = webdriver.Chrome()

    def open_website(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)

    def read_frames(self):
        # Switch to TOP frame
        self.driver.switch_to.frame("frame-top")

        # Switch to MIDDLE frame
        self.driver.switch_to.frame("frame-middle")
        middle_text = self.driver.find_element(By.ID, "content").text
        print("Middle Frame Text:", middle_text)

        # Back to top frame
        self.driver.switch_to.parent_frame()

        # Switch to RIGHT frame
        self.driver.switch_to.frame("frame-right")
        print("Right Frame Content Found")

        # Return to main page
        self.driver.switch_to.default_content()

        # Switch to BOTTOM frame
        self.driver.switch_to.frame("frame-bottom")
        bottom_text = self.driver.find_element(By.XPATH, "//body").text
        print("Bottom Frame Text:", bottom_text)

        time.sleep(3)


obj = HerokuIframePractice()
obj.open_website()
obj.read_frames()
