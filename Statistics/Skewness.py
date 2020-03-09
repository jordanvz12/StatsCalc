from Statistics.Statistics import mean
from Statistics.Statistics import standard_deviation
from Statistics.Statistics import mode
from Calculator.Division import division

#mode skewness  Pearson First Coefficient of Skewness
def skewness(data):
    meanMinusMode = mean(data) - mode(data)
    standardDeviation = standard_deviation(data)
    skewnessCoefficient = division(meanMinusMode, standardDeviation)
    return skewnessCoefficient

