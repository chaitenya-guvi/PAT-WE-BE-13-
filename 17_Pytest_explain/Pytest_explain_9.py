import pytest

"""
pytest-html
pytest-ordering

pip install pytest-html
syntax --html

> pytest .\17_Pytest_explain\Pytest_explain_9.py -s -v --html=htmlreport_new.html


"""


@pytest.fixture()
def setUP():
    print("\nthis is a Setup method at start\n")
    yield
    print("\nThis is a teardown \n ")


@pytest.mark.run(order=3)
def test_methodA(setUP):
    print("\n This is method A \n")


@pytest.mark.run(order=2)
def test_methodB(setUP):
    print("\n This is method B \n")


@pytest.mark.run(order=1)
def test_methodC(setUP):
    print("\n This is method C \n")