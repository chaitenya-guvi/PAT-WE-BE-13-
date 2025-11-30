"""
Pytest Fixtures Example
Fixtures in Pytest are used to set up a consistent and reusable test environment.
They help in preparing the necessary preconditions for tests and can also handle cleanup after tests are executed.
In this example, we define a fixture named `setUp` that prints a message before each test method runs.

When a test method includes `setUp` as a parameter,
Pytest automatically invokes the fixture before executing the test.
"""
import pytest

@pytest.fixture()
def setUp():
    print("\n\n%%%%%%%%%% Running demo1 setUp %%%%%%%%%%%%")

def test_demo1_methodA(setUp):
    print(" this is my test Running demo1 method A")
#
def test_demo2_methodB(setUp):
    print(" this is my test Running demo2 method B")
    a = 2
    assert a == 2

