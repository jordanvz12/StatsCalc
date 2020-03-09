import unittest
from numpy.random import seed
from numpy.random import randint
import random
from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        '''seed(5)
        self.testData = randint(0, 10, 20)'''
        random.seed(5)
        self.randomData = []
        i = 0
        while i < 6:
            self.randomData.append(random.randint(1, 100))
            i += 1
        #pprint.pprint(self.randomData)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

#test the mean
    def test_mean_calculator(self):
        mean = self.statistics.mean(self.randomData)
        self.assertEqual(mean, 73)
#test the median
    def test_median_calculator(self):
        median = self.statistics.median(self.randomData)
        self.assertEqual(median, 84.5)
#test the mode
    def test_mode_calculator(self):
        mode = self.statistics.mode(self.randomData)
        self.assertEqual(mode, 95)
#test the variance
    def test_variance_calculator(self):
        variance = self.statistics.variance(self.randomData)
        self.assertEqual(variance, 2235.5)

#test the standard deviation
    def test_standard_deviation_calculator(self):
        standard_deviation = self.statistics.standard_deviation(self.randomData)
        self.assertEqual(standard_deviation, 47.281074437876306)

    #def test_samplemean_calculator(self):
        #sample_mean = self.statistics.sample_mean(self.randomData)
        #self.assertEqual(sample_mean, 4.25)

#test the quartile function
    def test_quartliles_statistics(self):
        quartiles = self.statistics.quartile(self.randomData)
        self.assertEqual(quartiles, (54.5, 84.5, 93.5))

#test the skewness function (mode skewness)
    def test_skewness_statisitcs(self):
        skewness = self.statistics.skewness(self.randomData)
        self.assertEqual(skewness, -0.4653024547677381)

#test the sample correlation
    def test_samplecorrelation_statistics(self):
        correlation = self.statistics.sampleCorrelation(self.randomData, self.randomData) #should just be 1?
        self.assertEqual(correlation, 1.6112726459405051)
#test the zscore
    def test_zscore_statisitcs(self):
        zscore = self.statistics.zScore(self.randomData)
        self.assertEqual(zscore, 0.4653024547677381)

#test the mean deviation
    def test_meandeviation_statisitcs(self):
        meanDeviation = self.statistics.mean_deviation(self.randomData)
        self.assertEqual(meanDeviation, 2235.5)
    


if __name__ == '__main__':
    unittest.main()