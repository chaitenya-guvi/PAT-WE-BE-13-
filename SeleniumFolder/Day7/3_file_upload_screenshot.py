from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Initialize driver
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

wait = WebDriverWait(driver, 10)


file_path = os.path.abspath("random_data.txt")

# Wait for file input to be present
upload_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
upload_input.send_keys(file_path)

# Wait for Upload button and click
upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))
upload_button.click()

# Wait for confirmation message: "File Uploaded!"
confirmation = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
print("Upload Result:", confirmation.text)

# ----------------------------
# TAKE SCREENSHOT AFTER UPLOAD
# ----------------------------
timestamp = int(time.time())
screenshot_name = f"upload_result_{timestamp}.png"

driver.save_screenshot(screenshot_name)
print(f"Screenshot saved as: {screenshot_name}")

driver.quit()
