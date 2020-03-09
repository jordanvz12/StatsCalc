import unittest
from PopulationSampling.PopulationSampling import PopulationSampling
import random
import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.PopulationSampling = PopulationSampling()
        self.testData = []
        random.seed(5)
        i = 0
        while i < 11:
            self.testData.append(random.randint(1, 50))
            i += 1
        #pprint.pprint(self.testData)

        self.big_testData = []
        random.seed(6)
        i = 0
        while i < 100:
            self.big_testData.append(random.randint(1,100))
            i += 1


    def test_instantiate_statistics(self):
        self.assertIsInstance(self.PopulationSampling, PopulationSampling)

    #test simple random sampling
    def test_simplerandom_statistics(self):
        simpleRandomSample = self.PopulationSampling.simpleRandomSample(self.testData, 3)
        self.assertEqual(simpleRandomSample, [34, 40, 23])

    #test systematic sampling
    def test_systematicsampling_statistics(self):
        systematicSample = self.PopulationSampling.systematicSampling(self.big_testData, 10)
        self.assertEqual(systematicSample, [])

    #tests for the confidence interval for a sample
    def test_confidence_statistics(self):
        confidenceInterval = self.PopulationSampling.confidenceInterval(self.testData)
        self.assertEqual(confidenceInterval, (34.45454545454545, '=-', 32.60215984327236))

    #test for margin of error
    def test_marginoferror_statistics(self):
        marginError = self.PopulationSampling.margin_error(self.testData, 2)
        self.assertEqual(marginError, -22.94882917123613)

    #test cochrans sample size formula
    def test_samplesize_statistics(self):
        sampleSize = self.PopulationSampling.sample_size(self.big_testData, 0.5)
        self.assertEqual(sampleSize, 0.0)

#How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
    def test_samplesizeuknown_statistics(self):
        sample_size = self.PopulationSampling.sample_size_unknown(0.41, 0.95, 0.06)
        self.assertEqual(sample_size, 34.13703505262291)

#How to Find a Sample Size Given a Confidence Interval and Width (known population standard deviation)
    def test_samplesizeknown_statistics(self):
        sample_size = self.PopulationSampling.samplesizeKnownPop(self.big_testData, 0.99, 0.06)
        self.assertEqual(sample_size, 1599426.4255497276)

if __name__ == '__main__':
    unittest.main()