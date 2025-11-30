import pytest

# Define a list of tuples: (input_a, input_b, expected_output)
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),    # Test case 1
    (0, 0, 0),    # Test case 2
    (-1, 5, 4),   # Test case 3
    (10, -5, 5)   # Test case 4
])
def test_addition_multiple_inputs(a, b, expected):
    # Pytest will run this function four times, once for each tuple
    assert (a + b) == expected

# To run: `pytest test_simple.py`
# Pytest identifies this as 4 separate tests.