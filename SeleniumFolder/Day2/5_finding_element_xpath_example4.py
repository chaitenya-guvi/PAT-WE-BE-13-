from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.instagram.com/accounts/login/")

time.sleep(3)  # wait for page to load

# contains()
# search the submit button but i am not entering the entire text of submit button
login_button = driver.find_element(By.XPATH, "//button[contains(@type, 'sub')]")

# starts-with()
# search the input field whose name attribute starts with 'username'
input_field = driver.find_element(By.XPATH, "//input[starts-with(@name, 'username')]")

input_field.send_keys("sample_user")
time.sleep(2)
driver.quit()
