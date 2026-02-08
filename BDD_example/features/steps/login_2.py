from behave import given, when, then
from selenium.webdriver import Keys


@when(u'user enters invalid username and password')
def step_impl(context):
    webelement_username = context.driver.find_element("id", "user-name")
    webelement_username.clear()
    webelement_username.send_keys("error_user")
    webelement_password = context.driver.find_element("id", "password")
    webelement_password.clear()
    webelement_password.send_keys("secret_sauce")
    webelement_password.send_keys(Keys.ENTER)

@then(u'user should see error message')
def step_impl(context):
    error_message = context.driver.find_element("xpath", "//h3[@data-test='error']").text
    assert "Username and password do not match" in error_message
    context.driver.quit()