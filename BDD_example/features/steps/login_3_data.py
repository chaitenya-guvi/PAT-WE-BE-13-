from behave import given, when, then

from selenium.webdriver import Keys

@when('user enters username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element("id", "user-name").clear()
    context.driver.find_element("id", "user-name").send_keys(username)

    context.driver.find_element("id", "password").clear()
    context.driver.find_element("id", "password").send_keys(password)
    context.driver.find_element("id", "password").send_keys(Keys.ENTER)


@then('login result should be "{result}"')
def step_impl(context, result):

    if result == "success":
        assert "/inventory.html" in context.driver.current_url

    elif result == "locked_error":
        error_message = context.driver.find_element(
            "xpath", "//h3[@data-test='error']"
        ).text
        assert "Sorry, this user has been locked out." in error_message

    elif result == "invalid_error":
        error_message = context.driver.find_element(
            "xpath", "//h3[@data-test='error']"
        ).text
        assert "Username and password do not match" in error_message

    context.driver.quit()