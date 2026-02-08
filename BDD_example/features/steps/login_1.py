from behave.api.pending_step import StepNotImplementedError
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys


@given(u'user opens SauceDemo login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")


@when(u'user enters valid username and password')
def step_impl(context):
    webelement_username = context.driver.find_element("id", "user-name")
    webelement_username.clear()
    webelement_username.send_keys("standard_user")
    webelement_password = context.driver.find_element("id", "password")
    webelement_password.clear()
    webelement_password.send_keys("secret_sauce")
    webelement_password.send_keys(Keys.ENTER)

@then(u'user should land on inventory page')
def step_impl(context):
    try :
        assert  "/inventory.html" in context.driver.current_url
    finally:
        context.driver.quit()