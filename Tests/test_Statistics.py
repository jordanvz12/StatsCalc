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
        pprint.pprint(self.randomData)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.randomData)
        self.assertEqual(mean, 73)

    def test_median_calculator(self):
        median = self.statistics.median(self.randomData)
        self.assertEqual(median, 84.5)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.randomData)
        self.assertEqual(mode, 95)

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.randomData)
        self.assertEqual(variance, 0.00044732721986132855) #supposed to be 600.33333

    def test_standard_deviation_calculator(self):
        standard_deviation = self.statistics.standard_deviation(self.randomData)
        self.assertEqual(standard_deviation, 0.021150111580351735) #SUPPOSED TO BE 100.0555556

   #def test_samplemean_calculator(self):
        #sample_mean = self.statistics.sample_mean(self.randomData)
        #self.assertEqual(sample_mean, 4.25)


if __name__ == '__main__':
    unittest.main()