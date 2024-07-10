import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1,-1),-2)
        self.assertEqual(self.calc.add(1,-1),0)
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(3, 3), 0)
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(-2, 3), -5)
        self.assertEqual(self.calc.subtract(2, -3), 5)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(3, 2.5), 7.5)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 3), 0.66666666666666666666666666666667)
        self.assertEqual(self.calc.divide(3, 3), 1)
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(-2, 3), -0.66666666666666666666666666666667)
        self.assertEqual(self.calc.divide(2, 0), None)
        self.assertEqual(self.calc.divide(0, 3), None)

# Remember to write additional test methods for subtract, multiply, and divide.



if __name__ == "__main__":
    unittest.main()