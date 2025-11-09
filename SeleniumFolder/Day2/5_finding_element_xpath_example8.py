from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
ancestor:: - select parent elements

descendant:: - select child elements

following:: - select any element after the current node

preceding:: - select any element before the current node

parent:: - move upward to immediate

child:: - move downward to immediate children elements

"""


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

ancestor_form = driver.find_element(By.XPATH, "//input[@name='username']/ancestor::form")
print("Ancestor tag name:", ancestor_form.tag_name)
driver.quit()
