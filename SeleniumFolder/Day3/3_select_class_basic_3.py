import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class GlobalSQASelectExample:

    def __init__(self):
        self.url = "https://www.globalsqa.com/demo-site/select-dropdown-menu/"
        self.driver = webdriver.Chrome()

    def open_website(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)

    def select_by_visible_text(self):
        select_xpath = "//select"
        dropdown_element = self.driver.find_element(By.XPATH, select_xpath)

        select_obj = Select(dropdown_element)
        select_obj.select_by_visible_text("India")
        print("Selected option: India")
        time.sleep(3)

    def select_by_value(self):
        select_xpath = "//select"
        dropdown_element = self.driver.find_element(By.XPATH, select_xpath)

        select_obj = Select(dropdown_element)
        select_obj.select_by_value("USA")
        print("Selected option with value='USA'")
        time.sleep(3)

    def select_by_index(self):
        select_xpath = "//select"
        dropdown_element = self.driver.find_element(By.XPATH, select_xpath)

        select_obj = Select(dropdown_element)
        select_obj.select_by_index(5)
        print("Selected option by index 5")
        time.sleep(3)

        # Print all available dropdown values
        print("\nAvailable Dropdown Options:")
        for index, option in enumerate(select_obj.options):
            print(f"{index} --> {option.text}")

        print(f"\nTotal Options Count: {len(select_obj.options)}")




obj = GlobalSQASelectExample()
obj.open_website()

# Uncomment desired method to test
obj.select_by_visible_text()
# obj.select_by_value()
# obj.select_by_index()
