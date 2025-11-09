from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
following::tag — select any element after the current node
preceding::tag — select any element before the current node
ancestor::tag — move upward to parent elements
"""



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

password_input = driver.find_element(By.XPATH, "//input[@name='username']/following::input[@name='password']")
password_input.send_keys("password123")
time.sleep(2)
driver.quit()
