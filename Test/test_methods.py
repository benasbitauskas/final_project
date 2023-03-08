import unittest
from methods import *


class TestProblems(unittest.TestCase):

    def test_capitalize_input_tree_spp(self):
        self.assertEqual('P', capitalize_input_tree_spp('p'))
        self.assertEqual('BT', capitalize_input_tree_spp('bt'))
        self.assertEqual('PJ', capitalize_input_tree_spp('pJ'))
        with self.assertRaises(ValueError):
            capitalize_input_tree_spp(10)
        with self.assertRaises(ValueError):
            capitalize_input_tree_spp(7.8)

    def test_add_tree_volume(self):
        self.assertEqual([{'P': 100}], add_tree_volume('P', 100))
        self.assertEqual([{'P': 100}, {'B': 80}], add_tree_volume('B', 80))
        self.assertEqual([{'P': 100}, {'B': 80}, {'P': 100}], add_tree_volume('P', 100))
        with self.assertRaises(ValueError):
            add_tree_volume('B', -80)
        with self.assertRaises(KeyError):
            add_tree_volume('X', 80)

    def test_reduce_tree_volume_list(self):
        self.assertEqual({'B': 80, 'P': 200}, reduce_tree_volume_list())

    def test_sum_volume(self):
        self.assertEqual(280, sum_volume())

    def test_calculate_commercial_volume(self):
        self.assertEqual({'B': 66.4, 'P': 174.0}, calculate_commercial_volume())

    def test_sum_cvolume(self):
        self.assertEqual(240.4, sum_cvolume_total())

    def test_calculate_timber_price(self):
        self.assertEqual(56.79, calculate_timber_price(70.69, 13.90))

    def test_calculate_single_compensation(self):
        self.assertEqual(13652.32, calculate_single_compensation(70.69, 13.90))
        self.assertEqual(16993.88, calculate_single_compensation(70.69, 0))
        self.assertEqual(13702.8, calculate_single_compensation(70, 13))

    def test_calculate_annual_compensation(self):
        self.assertEqual(282.28, calculate_annual_compensation(2.06, 70, 13))
        self.assertEqual(137.03, calculate_annual_compensation(1, 70, 13))
        self.assertEqual('Kompensacija nemokama', calculate_annual_compensation(0, 70.69, 13.90))
        self.assertEqual('Kompensacija nemokama', calculate_annual_compensation(-2, 70.69, 0))

