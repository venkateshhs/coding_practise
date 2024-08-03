import unittest

# Function to be tested
def add(x, y):
    return x + y

# Test case class
class TestAddition(unittest.TestCase):

    # Test method
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)  # Assertion

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)  # Assertion

    def test_add_mixed_numbers(self):
        self.assertEqual(add(5, -3), 2)  # Assertion

# Entry point
if __name__ == '__main__':
    unittest.main()
