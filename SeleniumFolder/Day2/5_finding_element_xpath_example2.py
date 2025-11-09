from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")

search_button = driver.find_element(By.XPATH, "//input[@name='btnK' and @type='submit']")
print(search_button.get_attribute("value"))
driver.quit()
