import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class W3IframePractice:

    def __init__(self):
        self.url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe"
        self.driver = webdriver.Chrome()

    def open_website(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)

    def handle_iframe(self):
        # Switch to FIRST iframe containing "Iframe Example"
        self.driver.switch_to.frame("iframeResult")

        # Inside that frame, switch into inner iframe
        inner_frame = self.driver.find_element(By.XPATH, "//iframe")
        self.driver.switch_to.frame(inner_frame)

        link = self.driver.find_element(By.LINK_TEXT, "JAVASCRIPT")
        print("Clicking link inside iframe...")
        link.click()

        time.sleep(4)

        # Go back to main page
        self.driver.switch_to.default_content()
        print("Back to main content.")


obj = W3IframePractice()
obj.open_website()
obj.handle_iframe()
