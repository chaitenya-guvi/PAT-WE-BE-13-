import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize Chrome WebDriver
driver = webdriver.Firefox()
driver.maximize_window()

# Open OrangeHRM demo website
driver.get("https://opensource-demo.orangehrmlive.com/")

# Define an explicit wait with a maximum timeout of 10 seconds
wait = WebDriverWait(driver, 10) #basic explicit wait

start = time.time()

# Wait until the username field is visible and can be interacted with
try :
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "txtUsername")))
    # username_field=  driver.find_element(By.ID, "txtUsername")
    # username_field=  driver.find_element(By.NAME, "username")
except Exception as e:
    print("Exception occurred while waiting for username field:", str(e))
finally :
    end = time.time()
    print(f"Scipt took {end - start:.4f} seconds")