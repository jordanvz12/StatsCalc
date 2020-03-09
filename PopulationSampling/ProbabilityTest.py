import math
from Calculator.Calculator import division
from Calculator.Calculator import product
def normalProbabilityDensity(x):
    constant = division(1.0, math.sqrt(2*math.pi))
    return product(constant, math.exp((-x**2) / 2.0) )