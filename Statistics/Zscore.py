from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation
from Calculator.Calculator import division
from Calculator.Calculator import subtraction
import random
#z = (x – μ) / σ (thats the formula im using for zscore)
#https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/z-score/
def zScore(data):
    x = random.choice(data)
    meanData = mean(data)
    standardDeviation = standard_deviation(data)
    numerator = subtraction(x, meanData)
    z = division(numerator, standardDeviation)
    return z







