from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.google.com")
search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")
search_box.send_keys("Selenium WebDriver")
search_box.submit()

time.sleep(3)

first_result = driver.find_element(By.XPATH, "(//h3)[1]")
print(first_result.text)
driver.quit()
