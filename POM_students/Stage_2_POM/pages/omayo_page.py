"""
Page Object Model - Omayo Page (Level 2)

This page class contains:
- Element locators
- Page-specific actions
- Explicit waits for stability

Assertions are intentionally NOT included here.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OmayoPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------------- Locators ----------------

    search_box = (By.NAME, "q")
    search_submit = (By.XPATH, "//input[@type='submit']")

    table = (By.ID, "table1")
    table_rows = (By.XPATH, ".//tr")

    male_radio = (By.ID, "radio1")
    female_radio = (By.ID, "radio2")

    # ---------------- Actions ----------------

    def enter_search_text(self, text):
        search_box_element = self.wait.until(
            EC.element_to_be_clickable(self.search_box)
        )
        search_box_element.send_keys(text)

    def click_search_button(self):
        search_button = self.wait.until(
            EC.element_to_be_clickable(self.search_submit)
        )
        search_button.click()

    def get_table_rows_text(self):
        table_element = self.wait.until(
            EC.presence_of_element_located(self.table)
        )
        rows = table_element.find_elements(*self.table_rows)
        return [row.text for row in rows]

    def is_male_selected(self):
        male_radio = self.wait.until(
            EC.presence_of_element_located(self.male_radio)
        )
        return male_radio.is_selected()

    def is_female_selected(self):
        female_radio = self.wait.until(
            EC.presence_of_element_located(self.female_radio)
        )
        return female_radio.is_selected()
