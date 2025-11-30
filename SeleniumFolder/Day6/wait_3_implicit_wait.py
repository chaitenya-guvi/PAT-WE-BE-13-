from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com")

google_searchbox_webelement = driver.find_element(By.NAME, "q")
google_searchbox_webelement.send_keys("Selenium WebDriver", Keys.ENTER)

# Google results load dynamically but implicit wait handles presence
heading = driver.find_element(By.CSS_SELECTOR, "h3").text
print(heading)
print(driver.title)
