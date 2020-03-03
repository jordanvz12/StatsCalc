import unittest
from numpy.random import seed
from numpy.random import randint
import random
from RandomNums.RandomNums import RandomNums
import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.randomNums = RandomNums()

    def test_instantiate_random(self):
        self.assertIsInstance(self.randomNums, RandomNums)

    def test_noseedINT_random(self):
        noseedInt = self.randomNums.RandIntNoSeed() #how to test for a random number?
        self.assertEqual(noseedInt, 46457)

    def test_noseedDEC_random(self):
        noseedDec = self.randomNums.RandDecNoSeed()
        self.assertEqual(noseedDec, .4557)

    def test_seedINT_random(self):
        seedInt = self.randomNums.RandIntSeed()
        self.assertEqual(seedInt, 50)

    def test_seedDEC_random(self):
        seedDec = self.randomNums.RandDecSeed()
        self.assertEqual(seedDec, .5)




if __name__ == '__main__':
    unittest.main()