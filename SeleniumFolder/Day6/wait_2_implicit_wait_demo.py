from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def implicit_wait_demo():
    driver = webdriver.Chrome()

    # Setting implicit wait
    driver.implicitly_wait(10)     # <-- Applied only once, at driver level

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    # Click the START button
    driver.find_element(By.CSS_SELECTOR, "#start").click()

    # Now Selenium will wait up to 10s while trying to find the element
    text = driver.find_element(By.XPATH, "//div[@id='finish']/h4").text

    print("Loaded Text:", text)
    driver.quit()

implicit_wait_demo()
