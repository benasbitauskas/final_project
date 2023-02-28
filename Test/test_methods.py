import unittest
from methods import Data


class TestProblems(unittest.TestCase):

    def setUp(self):
        self.trees_vol1 = Data('P', 100)
        self.trees_vol2 = Data('D', 60.5)
        self.trees_vol3 = Data('B', -80)
        self.trees_vol4 = Data('X', 80)
        # self.ldict1 = [{'P': 87.0}, {'P': 87.0}]
        # self.ldict2 = [{'D': 87.0}, {'B': 83.0}]

    def test_calculate_lvolume(self):
        self.assertEqual(self.trees_vol1.calculate_lvolume(), 87)
        self.assertEqual(self.trees_vol2.calculate_lvolume(), 52.63)
        with self.assertRaises(ValueError):
            self.trees_vol3.calculate_lvolume()
        with self.assertRaises(KeyError):
            self.trees_vol4.calculate_lvolume()

    # def test_sum_lvolume_total(self):







