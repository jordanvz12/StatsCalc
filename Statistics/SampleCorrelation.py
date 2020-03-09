from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation
from Calculator.Calculator import product
from Calculator.Calculator import division
from Calculator.Calculator import subtraction
#from numpy import cov
def sampleCorrelation(dataX, dataY):
    #dataX= []
    #dataY = []
    meanX = mean(dataX)
    meanY = mean(dataY)
    deviationX = standard_deviation(dataX)
    deviationY = standard_deviation(dataY)
    rNumerator = 0.0
    for i in range(len(dataX)):
        rNumerator += product(subtraction(dataX[i],meanX), subtraction(dataY[i], meanY))
    rDenominator = product(deviationX, deviationY)
    r = division(rNumerator, rDenominator)
    return r
    #covariance = cov(dataOne, dataTwo)

