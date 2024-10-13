import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Positive and negative
        self.assertEqual(self.calc.add(0, 0), 0)  # Edge case: adding zero
        self.assertEqual(self.calc.add(-5, -3), -8)  # Negative numbers

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Positive numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)  # Positive and negative
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Edge case: subtracting zero
        self.assertEqual(self.calc.subtract(-5, -3), -2)  # Negative numbers

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Positive numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)  # Positive and negative
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Edge case: multiplying by zero
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # Negative numbers

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 2), 3.0)  # Normal division
        self.assertEqual(self.calc.divide(-6, 2), -3.0)  # Positive and negative
        self.assertEqual(self.calc.divide(0, 1), 0.0)  # Edge case: zero numerator
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero returns None

    def test_divide_by_zero(self):
        """Test dividing by zero."""
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero returns None

if __name__ == "__main__":
    unittest.main()
