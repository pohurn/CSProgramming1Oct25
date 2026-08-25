# contains the tests.

# Import Python's built-in unittest library.
import unittest

# Import the add function from calculator.py.
from calculator import add


# Create a class containing our tests.
# Our class must inherit from unittest.TestCase.
class TestCalculator(unittest.TestCase):

    # Create a test method.
    # Test methods should normally start with the word test.
    def test_add(self):

        # Call our add function.
        result = add(2, 3)

        # Check whether the result is equal to 5.
        self.assertEqual(result, 5)
        # assertEqual(ACTUAL, EXPECTED)


# Run the tests when this file is executed.
if __name__ == "__main__":

    # Start unittest.
    unittest.main()


# READ ABOUT ASSERTIONS
# - assertEqual(a, b) => a should be equal to b
# - assertNotEqual(a, b) => a should not be equal to be
# - assertTrue(x) => x should be True
# - assertFalse(y) => y should be false
# - assertIsNone(v) => v should be none
# - assertIn(a,b) => a should be in b
