# Import the pytest library
import pytest

# Example function to be tested
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test case for the `add` function
def test_add():
    # Assert that the result of add(2, 3) is 5
    assert add(2, 3) == 5
    # Assert that the result of add(-1, 1) is 0
    assert add(-1, 1) == 0

# Test case for the `subtract` function
def test_subtract():
    # Assert that the result of subtract(5, 3) is 2
    assert subtract(5, 3) == 2
    # Assert that the result of subtract(0, 1) is -1
    assert subtract(0, 1) == -1

# Using pytest fixtures to set up reusable test data
@pytest.fixture
def sample_data():
    # Return a dictionary with sample data
    return {"a": 10, "b": 5}

# Test case using the fixture
def test_add_with_fixture(sample_data):
    # Use the fixture data to test the add function
    assert add(sample_data["a"], sample_data["b"]) == 15

# Parameterized test to run the same test logic with different inputs
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),  # Test case 1
    (0, 0, 0),  # Test case 2
    (-1, -1, -2)  # Test case 3
])
def test_add_parametrized(a, b, expected):
    # Assert that the add function works for all parameterized inputs
    assert add(a, b) == expected

#Run this file with `pytest <filename>.py` to execute the tests.