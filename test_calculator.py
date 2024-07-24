# tests/test_calculator.py
import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_addition_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_addition_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_addition_fail(self):
        self.assertEqual(add(2, 2), 5)

    def test_addition_fail2(self):
        self.assertEqual(add(-2, 2), 0)

if __name__ == '__main__':
    unittest.main()
