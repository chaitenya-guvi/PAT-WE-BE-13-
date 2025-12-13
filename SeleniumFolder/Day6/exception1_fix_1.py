from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-exceptions/")

# Click Add button
driver.find_element(By.ID, "add_btn").click()

wait = WebDriverWait(driver, 10)

# Wait until Row 2 input field is visible
row2_input = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='row2']//input"))
)

# Verification
assert row2_input.is_displayed()

driver.quit()
