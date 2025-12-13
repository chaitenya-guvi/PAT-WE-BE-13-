from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-exceptions/")

# Click Add button
driver.find_element(By.ID, "add_btn").click()

# No wait added here
# Row 2 input field appears after a delay

row2_input = driver.find_element(By.XPATH, "//div[@id='row2']//input")

# Verification
assert row2_input.is_displayed()

driver.quit()
