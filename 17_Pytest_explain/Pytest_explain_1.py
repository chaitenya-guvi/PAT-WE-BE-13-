"""
Pytest is a popular testing framework in Python used to write and run automated tests.
It is mainly used for:

Unit testing (testing small pieces of code like functions)

Integration testing (testing how components work together)

API testing

pip install pytest
pip install pytest-html   # for html reports
pip install pytest-ordering  # for test case ordering
"""""


def add(a, b):
    return a + b


def test_addition():
    assert add(2, 3) == 5

