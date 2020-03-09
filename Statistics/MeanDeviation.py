from Statistics.Statistics import mean
from Calculator.Calculator import subtraction
from Calculator.Calculator import division
from Calculator.Calculator import addition
from Calculator.Calculator import power

def meanDeviation(data):
    global summation
    num_values = len(data)
    xbar = mean(data)
    willSquare = []
    squared = []
    for items in data:
        willSquare.append(abs(subtraction(items, xbar)))
        for values in willSquare:
            squared.append(power(values, 2))
            summation = sum(squared)
    return division(summation, num_values)
