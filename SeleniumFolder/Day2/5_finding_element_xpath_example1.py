from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.google.com")

# Absolute XPath (not recommended)
# absolute xpath starts with '/' which means search from root element
search_box = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/form/div[1]/div[1]/div[1]/div[1]/textarea")

# Relative XPath (preferred)
#  relative xpath starts with '//' which means search from anywhere in the document
search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")

search_box.send_keys("Selenium Python")
time.sleep(2)
driver.quit()



