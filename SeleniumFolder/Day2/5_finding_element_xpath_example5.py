from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

# locating input within parent div
username_input = driver.find_element(By.XPATH, "//form[@id='loginForm']//input[@name='username']")
username_input.send_keys("test_username")
time.sleep(2)
driver.quit()
