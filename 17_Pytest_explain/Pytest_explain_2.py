"""
| Feature                 | Description                                                                |
| ----------------------- | -------------------------------------------------------------------------- |
| Simple syntax           | Tests are written as normal Python functions                               |
| Auto-test discovery     | Pytest automatically finds files named `test_*.py` or `*_test.py`          |
| Rich assertion messages | Failing tests show clear, helpful output                                   |
| Supports fixtures       | Reusable setup and cleanup code                                            |
| Plugins support         | Thousands of plugins available (pytest-html, pytest-xdist, allure reports) |
| Parameterization        | Run the same test with multiple inputs easily                              |

"""

# assert example using pytest
# expected to fail
def test_string_check():
    text = "pytest"
    assert text == "python"


def test_string_check_2():
    text = "python"
    assert text == "python"
