import pytest

"""
pip install pytest-ordering

syntax --html

>pytest -s -v pytest_trial\test_pytest_demo.py --html=htmlreport_new.html


"""


@pytest.fixture()
def setUP():
    print("\n @@@@@@@ This is a Setup method at start\n")
    yield
    print("\n @@@@@@@ This is a teardown \n ")


# @pytest.mark.run(order=3)
def test_methodA(setUP):
    print("\n This is method A \n")


# @pytest.mark.run(order=2)
def test_methodB(setUP):
    print("\n This is method B \n")


@pytest.mark.run(order=1)
def test_methodC(setUP):
    print("\n This is method C \n")