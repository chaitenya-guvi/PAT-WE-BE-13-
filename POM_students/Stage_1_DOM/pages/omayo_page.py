"""
Page Object Model (POM) - Omayo Page

Purpose:
--------
This file represents the Omayo web page.
It contains ONLY:
- Element locators
- Methods to perform actions on the page

What should NOT be here:
------------------------
- Assertions
- Test validation logic
- Hardcoded test data

Why POM:
--------
- Keeps locators in one place
- Improves code reusability
- Makes tests easy to maintain when UI changes

Rule:
-----
One page = One class
"""

from selenium.webdriver.common.by import By


class OmayoPage:

    def __init__(self, driver):
        """
        Constructor to initialize the WebDriver instance.

        :param driver: Selenium WebDriver object
        """
        self.driver = driver

    # ------------------- Locators -------------------

    search_box = (By.NAME, "q")
    search_submit = (By.XPATH, "//input[@type='submit']")

    table = (By.ID, "table1")
    table_rows = (By.XPATH, ".//tr")

    male_radio = (By.ID, "radio1")
    female_radio = (By.ID, "radio2")

    # ------------------- Actions -------------------

    def enter_search_text(self, text):
        """
        Enters text into the search box.

        :param text: text to be searched
        """
        self.driver.find_element(*self.search_box).send_keys(text)

    def click_search_button(self):
        """
        Clicks on the search submit button.
        """
        self.driver.find_element(*self.search_submit).click()

    def get_table_rows_text(self):
        """
        Fetches text from all rows of the table.

        :return: List of row text values
        """
        table_element = self.driver.find_element(*self.table)
        rows = table_element.find_elements(*self.table_rows)
        return [row.text for row in rows]

    def is_male_selected(self):
        """
        Checks if male radio button is selected.

        :return: True if selected, else False
        """
        return self.driver.find_element(*self.male_radio).is_selected()

    def is_female_selected(self):
        """
        Checks if female radio button is selected.

        :return: True if selected, else False
        """
        return self.driver.find_element(*self.female_radio).is_selected()
