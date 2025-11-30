"""
file name should start with test
test method name should start with test

pytest test_mod.py   # run tests in module
 - pytest .\Pytest_explain_3.py

pytest somepath      # run all tests below somepath
 - pytest .\16_Pytest_explain\Pytest_explain_3.py

pytest test_module.py::test_method  # only run test_method in test_module
 - pytest .\16_Pytest_explain\Pytest_explain_3.py::test_add_positive_numbers

-s to print statements
-v verbose


Files, Files must be named starting with test_ or ending with _test.py.
Functions/Methods, Functions and methods must be named starting with test_.

"""

# Function to be tested (usually in a separate file, but kept here for simplicity)
def add(a, b):
    return a + b

# The test function
def test_add_positive_numbers():
    # The assertion is key. If True, the test passes. If False, it fails.
    print("hello world")
    assert add(5, 3) == 8

def test_add_negative_numbers():
    assert add(-1, -4) == -5

# To run: `pytest Pytest_explain_3.py -v -s`
