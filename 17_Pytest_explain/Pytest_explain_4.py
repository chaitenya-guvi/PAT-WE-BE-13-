"""
Pytest fixture

A fixture in pytest is a reusable function that provides test data or setup code for your tests.
It runs before the test function, and whatever it returns becomes available to the test.

Fixtures in Pytest are a way to provide a fixed baseline
 upon which tests can reliably and repeatedly execute.

NOTE : They are used to set up preconditions needed for tests and to clean up after tests have run.
"""

"""
Workflow  : 
1. I am declaring a fixture named `sample_data` using the `@pytest.fixture` decorator.
2. The fixture function returns a list `[1, 2, 3]`.
3. The test function `test_list` takes `sample_data` as an argument.
4. When `test_list` is executed, pytest automatically calls the `sample_data` fixture
   and passes its return value to the test function.

5. The test then asserts that the length of the list is 3.

"""

import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_list(sample_data):
    assert len(sample_data) == 3


