from Statistics.Statistics import variance
from Calculator.Calculator import root
def standard_deviation(data):
    return root(variance(data), 2)

