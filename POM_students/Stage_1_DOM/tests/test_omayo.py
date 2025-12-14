"""
Test File - Omayo Page Tests

Purpose:
--------
This file contains test cases for Omayo page.

Responsibilities:
------------------
- Call page class methods
- Perform assertions
- Decide test pass or fail

What should NOT be here:
------------------------
- Web element locators
- Low-level UI interaction logic

Best Practice:
--------------
Tests should read like steps of a test case.
Assertions should always remain in test files.
"""

from selenium import webdriver
from POM_students.Stage_1_DOM.pages.omayo_page import OmayoPage


def test_verify_search_textbox():
    """
    TC: Verify that the 'Search this blog' text field
    is clickable and allows entering a value.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")

    omayo = OmayoPage(driver)
    omayo.enter_search_text("Sharon")
    omayo.click_search_button()

    assert driver.current_url == "https://omayo.blogspot.com/search?q=Sharon"

    driver.quit()


def test_verify_table_first_column_value():
    """
    TC: Verify that the first column in the table
    contains the value 'Kishore'.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")

    omayo = OmayoPage(driver)
    rows_text = omayo.get_table_rows_text()

    assert "Kishore" in rows_text[1]

    driver.quit()


def test_verify_radio_buttons_not_selected_by_default():
    """
    TC: Verify that no gender radio button
    is selected by default.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")

    omayo = OmayoPage(driver)

    assert not omayo.is_male_selected(), "Male radio button is selected"
    assert not omayo.is_female_selected(), "Female radio button is selected"

    driver.quit()
