from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.StandardDeviation import standard_deviation
from Statistics.Quartiles import quartiles
from Statistics.Skewness import skewness
from Statistics.SampleCorrelation import sampleCorrelation
from Statistics.Zscore import zScore
from Statistics.MeanDeviation import meanDeviation

class Statistics(Calculator):

    def __init__(self):
        super().__init__()
        self.data = None

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result

    def quartile(self, data):
        self.result = quartiles(data)
        return self.result

    def skewness(self, data):
        self.result = skewness(data)
        return self.result

    def sampleCorrelation(self, dataX, dataY):
        self.result = sampleCorrelation(dataX, dataY)
        return self.result

    def zScore(self, data):
        self.result = zScore(data)
        return self.result

    def mean_deviation(self, data):
        self.result = meanDeviation(data)
        return self.result