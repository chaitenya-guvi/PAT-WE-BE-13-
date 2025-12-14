"""TC: 1Verify that the ‘Search this blog’
text field is clickable and allows entering a value."""

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sharon_TC() :
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://omayo.blogspot.com/"

    driver.get(url)

    locator_seracbox= (By.NAME,"q")
    search_button_webelement = driver.find_element(*locator_seracbox)

    search_button_webelement.send_keys("Sharon")

    locator_searchbox_submit_button = (By.XPATH, "//input[@type='submit']")
    search_button_submit_webelement = driver.find_element(*locator_searchbox_submit_button)
    search_button_submit_webelement.click()

    assert driver.current_url == "https://omayo.blogspot.com/search?q=Sharon"

def test_Shubham_TC():

    """
    test case to verify the first column in table has value 'Kishore'

    :return:
    """
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://omayo.blogspot.com/"

    driver.get(url)

    locator_table = (By.ID, "table1")
    table_webelement = driver.find_element(*locator_table)

    locator_row = (By.XPATH, "//tr")
    first_column_value = table_webelement.find_elements(*locator_row)

    text_of_first_row = first_column_value[0].text
    text_of_second_row = first_column_value[1].text
    print(text_of_first_row)
    print(text_of_second_row)

    assert "Kishore" in text_of_second_row

def test_Kalai_TC():
    """
    verifying that no radio button is selected by default for gender
    :return:
    """
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://omayo.blogspot.com/"

    driver.get(url)

    locator_radio_button_male = (By.ID, "radio1")
    locator_radio_button_female = (By.ID, "radio2")

    male_radio_button_webelement = driver.find_element(*locator_radio_button_male)
    female_radio_button_webelement = driver.find_element(*locator_radio_button_female)


    male_radio_button_webelement.click()
    # neither radio button should be selected by default
    assert not male_radio_button_webelement.is_selected() , "male is selected"
    assert not female_radio_button_webelement.is_selected(), "female is selcted"


