import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        add = self.calculator.add(4 ,6)
        self.assertEqual(add, 10)

    def test_subtraction(self):
        subtract = self.calculator.subtract(6 ,3)
        self.assertEqual(subtract, 3)

    def test_division(self):
        divide = self.calculator.divide(10, 2)
        self.assertEqual(divide, 5)

    def test_multiplication(self):
        product = self.calculator.multiply(3, 3)
        self.assertEqual(product, 9)

    def test_power(self):
        power = self.calculator.square(3, 2)
        self.assertEqual(power, 9)

    def test_root(self):
        root = self.calculator.root(9, 2)
        self.assertEqual(root, 3)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()