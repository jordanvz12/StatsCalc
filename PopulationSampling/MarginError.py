from Statistics.Statistics import zScore
from Statistics.Statistics import standard_deviation
from Calculator.Calculator import product
from Calculator.Calculator import division
from Calculator.Calculator import root

def margin_error(data, sample_size):
    zscore = zScore(data)
    standardDeviation = standard_deviation(data)
    denominator = root(sample_size, 2)
    willMultiply = division(standardDeviation, denominator)
    marginOfError = product(zscore, willMultiply)
    return marginOfError