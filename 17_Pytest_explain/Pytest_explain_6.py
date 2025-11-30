"""
Pytest Fixture Example

Yield can be used in Pytest fixtures to define setup and teardown behavior for tests.
When a fixture uses yield, the code before the yield statement is executed before the test runs (setup),
and the code after the yield statement is executed after the test completes (teardown).

In this example, we define a fixture named `setUp` that prints a message before and after each test method runs.
When a test method includes `setUp` as a parameter, Pytest automatically invokes the fixture
before and after executing the test.

"""
import pytest


@pytest.fixture()
def setUp():
    print("\n\n @@@@@@@@@ Running demo2 setUp befor my test ^^^^^^^^^")
    yield
    print("\n\n %%%%%%%%% after my test numer 1  Running demo2 tearDown!!!!!!!!!!!!!")

def test_demo2_methodA(setUp):
    print(" actual test Running demo2 method A************")

def test_demo2_methodB(setUp):
    print("********* test number 2 Running demo2 method B")