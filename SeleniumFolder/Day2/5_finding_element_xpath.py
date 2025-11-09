""" xpath - "https://www.guru99.com/xpath-selenium.html#7" """


"""
XPath or XML Path is a query language for selecting nodes from an XML document.
 
 In Selenium, XPath is used to navigate through elements and attributes in an HTML document.
//tag[@attribute='value']

//tag[@attribute1='value']
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


"""
identify using xpath
"""


url = "https://www.instagram.com/"

driver = webdriver.Firefox()
# Open the webpage to url
driver.get(url)
sleep(2)

#maximise window
driver.maximize_window()

webelement_of_email_input = driver.find_element(By.XPATH,"//input[@name='username']")
webelement_of_email_input.send_keys("999999999")

#
webelement_of_password_input = driver.find_element(By.XPATH,'//input[@type="password"]')
webelement_of_password_input.send_keys("examplepassword")




