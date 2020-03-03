from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Statistics.Statistics import mean
from Calculator.Power import power

def variance(data):
    global summation
    num_values = len(data)
    xbar = mean(data)
    willSquare = []
    squared = []
    for items in data:
        willSquare.append(subtraction(items, xbar))
        for values in willSquare:
            squared.append(power(values, 2))
            summation = sum(squared)
    return division(summation, num_values)







