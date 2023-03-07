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


# test_list = [{'P': 100}, {'P': 100}, {'B': 100}, {'D': 100}]
# new_dict = {'P': 200, 'B': 100, 'D': 100}
# average_price = 70.69
# preparation_price = 13.90
# lvolume = {'P': 174.0, 'B': 83.0, 'D': 87.0}
# lvolume_total = 344
# t_price = 56.79
# interest = 2.06
# print(add_tree_volume('P', 100))
# print(add_tree_volume('P', 100))
# print(add_tree_volume('B', 100))
# print(add_tree_volume('D', 100))
# print(f'2: {reduce_tree_volume_list()}')
# print(f'3: {sum_volume_total()}')
# print(f'4: {calculate_commercial_volume()}')
# print(f'5: {sum_cvolume_total()}')
# print(f'6: {calculate_timber_price(average_price, preparation_price)}')
# print(f'7: {calculate_single_compensation()}')
# print(f'8: {calculate_annual_compensation(interest)}')
