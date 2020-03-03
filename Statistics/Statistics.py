from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.StandardDeviation import standard_deviation
from Statistics.SampleMean import sample_mean


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


    #def sample_mean(self, sample_size):
       #self.result = sample_mean(self.data, sample_size)
        #return self.result

