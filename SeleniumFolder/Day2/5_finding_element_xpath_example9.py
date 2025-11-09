from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.google.com")

search_box = driver.find_element(By.XPATH, "//textarea[contains(@class, 'gLFyf') and @name='q']")
search_box.send_keys("Python Selenium advanced xpath")
search_box.submit()

time.sleep(3)

# get titles that contain 'Selenium'
titles = driver.find_elements(By.XPATH, "//h3[contains(text(), 'Selenium')]")
for t in titles:
    print(t.text)
driver.quit()
