import unittest
from methods import TreeSppVolume


class TestProblems(unittest.TestCase):

    def setUp(self):
        self.trees_vol1 = TreeSppVolume('P', 100)
        self.trees_vol2 = TreeSppVolume('D', 60.5)
        self.trees_vol3 = TreeSppVolume('B', -80)
        self.trees_vol4 = TreeSppVolume('X', 80)

    def test_calculate_lvolume(self):
        self.assertEqual(self.trees_vol1._calculate_lvolume(), 87.0)
        self.assertEqual(self.trees_vol2._calculate_lvolume(), 52.635)
        with self.assertRaises(ValueError):
            self.trees_vol3._calculate_lvolume()
        with self.assertRaises(KeyError):
            self.trees_vol4._calculate_lvolume()

    def test_sum_lvolume_total(self):
        self.assertEqual(self.trees_vol1._sum_lvolume_total(), 139.63)
        self.assertEqual(self.trees_vol4._sum_lvolume_total(), 139.63)
