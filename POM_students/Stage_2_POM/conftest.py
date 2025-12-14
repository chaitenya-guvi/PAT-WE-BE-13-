"""
conftest.py

Purpose:
--------
Centralized pytest configuration file.

Responsibilities:
------------------
- WebDriver setup and teardown
- Provide driver fixture to tests
- Avoid code duplication across test files

Note:
-----
pytest automatically discovers this file.
No import is required in test files.
"""

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")
    yield driver
    driver.quit()
