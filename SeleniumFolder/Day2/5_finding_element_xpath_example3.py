from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# using text() function in xpath
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")

images_link = driver.find_element(By.XPATH, "//a[text()='Images']")
images_link.click()
time.sleep(2)
driver.quit()
