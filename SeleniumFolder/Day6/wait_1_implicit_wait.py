"""
implicit wait
is a type of wait that is set for the lifetime of the WebDriver object.
It tells the WebDriver to wait for a certain amount of time when trying
to find an element if it is not immediately available.

- defined once
- impacts all element searches
- used for handling dynamic content loading
- applicable for the lifetime of the WebDriver instance
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select"
driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get(url)

driver.switch_to.frame("iframeResult")

dropdown = driver.find_element(By.ID, "cars")
dropdown.click()
