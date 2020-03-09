from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Power import power
from Calculator.Root import root
from Calculator.Multiplication import product


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a,b)
        return self.result

    def square(self, a, b):
        self.result = power(a,b)
        return self.result

    def root(self, a, b):
        self.result = root(a,b)
        return self.result

    def multiply(self, a, b):
        self.result = product(a,b)
        return self.result