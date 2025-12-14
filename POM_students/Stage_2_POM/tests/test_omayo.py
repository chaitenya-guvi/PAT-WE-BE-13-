"""
Test File - Omayo Tests (Level 2 POM)

Responsibilities:
------------------
- Use page methods
- Perform assertions
- Validate application behavior

No locators or Selenium low-level code here.
"""

from POM_students.Stage_2_POM.pages.omayo_page import OmayoPage


def test_verify_search_textbox(driver):
    """
    TC: Verify that the 'Search this blog' text field
    is clickable and allows entering a value.
    """
    omayo = OmayoPage(driver)

    omayo.enter_search_text("Sharon")
    omayo.click_search_button()

    assert driver.current_url == "https://omayo.blogspot.com/search?q=Sharon"


def test_verify_table_first_column_value(driver):
    """
    TC: Verify that the first column in the table
    contains the value 'Kishore'.
    """
    omayo = OmayoPage(driver)
    rows_text = omayo.get_table_rows_text()

    assert "Kishore" in rows_text[1]


def test_verify_radio_buttons_not_selected_by_default(driver):
    """
    TC: Verify that no gender radio button
    is selected by default.
    """
    omayo = OmayoPage(driver)

    assert not omayo.is_male_selected(), "Male radio button is selected"
    assert not omayo.is_female_selected(), "Female radio button is selected"

def test_another_without_fixture():
    """
    this is a

    :return:
    """