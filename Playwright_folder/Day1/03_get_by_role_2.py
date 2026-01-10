from playwright.sync_api import sync_playwright, expect
"""
AAA

Arrange
Act
Assert

"""

def test_saucedemo_login_get_by_role():
    with sync_playwright() as p:
        # Launch Chromium browser with headless mode off

        browser = p.chromium.launch()

        # browser = p.chromium.launch(headless=False,slow_mo=5000)
        # Create a new browser context and page
        """
        What is context in Playwright?
        A browser context in Playwright is an isolated environment within a browser instance.
        It allows you to create multiple independent sessions with separate cookies, cache, and storage,
        enabling parallel testing and better resource management.
        """
        context = browser.new_context()
        

        """
        what is page in Playwright?
        A page in Playwright represents a single tab or window within a browser context.
        It provides an interface to interact with web content, allowing you to navigate,
        manipulate elements, and perform actions such as clicking, typing, and taking screenshots.
        """
        page = context.new_page()

        # Open SauceDemo
        page.goto("https://www.saucedemo.com/")
        page.go_back()
        page.go_forward()


        """
        what are load states in Playwright?
        Load states in Playwright refer to the different stages of a web page's loading process.
        Playwright provides methods to wait for specific load states, such as 'load', 'dom
        content loaded', and 'network idle', ensuring that actions are performed only when the page is ready.
        """
        page.wait_for_load_state("domcontentloaded")
        assert page.url == "https://www.saucedemo.com/"
        expect(page).to_have_title("Swag Labs")


        # ---------------- BASIC get_by_role ----------------



        # 1. Enter username
        page.get_by_role("textbox", name="Username").fill("standard_user")
        page.fill('input[data-test="username"]', 'hello')
        # page.get_by_test_id("username").fill("test id text")
        page.get_by_placeholder("Username").fill("filled by placeholder")
        # exact match
        page.get_by_text("Login",exact=True).click()
        #partial match
        page.get_by_text("Log",exact=False).click()

        # 2. Enter password
        page.get_by_role("textbox", name="Password").fill("secret_sauce")
        page.get_by_role("textbox", name="Username").fill("standard_user")

        # 3. Click Login button
        page.get_by_role("button", name="Login").click()

        # ---------------- VERIFICATION ----------------

        # Verify successful login
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

        # Cleanup
        context.close()
        browser.close()


if __name__ == "__main__":
    test_saucedemo_login_get_by_role()
