import unittest
from numpy.random import seed
from numpy.random import randint
import random
from RandomNums.RandomNums import RandomNums
import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.randomNums = RandomNums()
        self.testData = []
        random.seed(10)
        i = 0
        while i < 11:
            self.testData.append(random.randint(1, 100))
            i += 1
        #pprint.pprint(self.testData)

    def test_instantiate_random(self):
        self.assertIsInstance(self.randomNums, RandomNums)

    def test_noseedINT_random(self):
        noseedInt = self.randomNums.RandIntNoSeed() #how to test for a random number?
        #self.assertEqual(noseedInt, 42)
        pprint.pprint(noseedInt)

    def test_noseedDEC_random(self):
        noseedDec = self.randomNums.RandDecNoSeed()
        #self.assertEqual(noseedDec, .4557)
        pprint.pprint(noseedDec)

    def test_seedINT_random(self):
        seedInt = self.randomNums.RandIntSeed()
        self.assertEqual(seedInt, 16)

    def test_seedDEC_random(self):
        seedDec = self.randomNums.RandDecSeed()
        self.assertEqual(seedDec, 0.23796462709189137)

    def test_randomList_random(self):
        randList = self.randomNums.RangeNums()
        pprint.pprint(randList)

    def test_randomItem_random(self):
        randomItem = self.randomNums.RandomItem()
        pprint.pprint(randomItem)

    def test_randomSelectwithSeed_random(self):
        randomSelect = self.randomNums.RandomSelect()
        self.assertEqual(randomSelect, 35)

    def test_noseedNItems_random(self):
        nItemsNoSeed = self.randomNums.NItemsNoSeed(self.testData, 2)
        self.assertEqual(nItemsNoSeed, [2, 74])

    def test_nItemsSeed_random(self):
        nItemsSeed = self.randomNums.NItemsSeed(self.testData, 2)
        self.assertEqual(nItemsSeed, [36, 63])

if __name__ == '__main__':
    unittest.main()