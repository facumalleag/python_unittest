import unittest
from src.calculator import add, subtract, div, multiply


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_div(self):
        self.assertEqual(div(10, 5), 2)

    def test_div_por_cero(self):
        with self.assertRaises(ValueError) as cm:
            div(10, 0)
        self.assertEqual(str(cm.exception), "La division por cero no esta permitida")

    def test_multiply(self):
        self.assertEqual(multiply(9, 3), 27)
