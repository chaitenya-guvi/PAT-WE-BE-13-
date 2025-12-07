from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()

# Open URL
driver.get("https://the-internet.herokuapp.com/upload")

# Prepare file path (file must exist on your machine)
# file_path = os.path.abspath("sample.txt")    # put your file name here
file_path = "C:\\Users\\LENOVO\\PycharmProjects\\PAT-WE-BE-13-\\SeleniumFolder\\Day7\\random_data.txt"



# Upload the file
choose_folder_webelement = driver.find_element(By.ID, "file-upload")
choose_folder_webelement.send_keys(file_path)

# Click Upload button
driver.find_element(By.ID, "file-submit").click()


# Just wait for visibility
time.sleep(3)

# Validate upload success
result = driver.find_element(By.TAG_NAME, "h3").text
print("Result:", result)
driver.quit()