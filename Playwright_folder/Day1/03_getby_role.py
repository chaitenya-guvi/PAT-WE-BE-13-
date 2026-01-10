from playwright.sync_api import sync_playwright, expect


def test_saucedemo_login_get_by_role():
    with sync_playwright() as p:
        # Launch Chromium browser with headless mode off

        browser = p.chromium.launch(headless=False,slow_mo=200)
        # Create a new browser context and page
        """
        What is context in Playwright?
        A browser context in Playwright is an isolated environment within a browser instance.
        It allows you to create multiple independent sessions with separate cookies, cache, and storage,
        enabling parallel testing and better resource management.
        """
        context1 = browser.new_context()
        context2 = browser.new_context()

        """
        what is page in Playwright?
        A page in Playwright represents a single tab or window within a browser context.
        It provides an interface to interact with web content, allowing you to navigate,
        manipulate elements, and perform actions such as clicking, typing, and taking screenshots.
        """
        page1 = context1.new_page()

        # Open SauceDemo
        page1.goto("https://www.saucedemo.com/")
        page1.get_by_role("textbox", name="Username").fill("standard_user")

        page2 = context1.new_page()
        page2.goto("https://the-internet.herokuapp.com/dropdown")

        """
        what are load states in Playwright?
        Load states in Playwright refer to the different stages of a web page's loading process.
        Playwright provides methods to wait for specific load states, such as 'load', 'dom
        content loaded', and 'network idle', ensuring that actions are performed only when the page is ready.
        """
        page.wait_for_load_state("domcontentloaded")


        # ---------------- BASIC get_by_role ----------------



        # 1. Enter username
        page.get_by_role("textbox", name="Username").fill("standard_user")
        page.fill('input[data-test="username"]', 'hello')

        # 2. Enter password
        page.get_by_role("textbox", name="Password").fill("secret_sauce")

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
