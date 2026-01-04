import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dropdown")
    expect(page.get_by_role("heading", name="Dropdown List")).to_be_visible()