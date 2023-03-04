from settings import liquid_t
from math import fsum
import collections
import functools
import operator

# import logs as lg

tree_volume_list = []
tree_commercial_volume_list = []


def add_tree_volume(tree_spp, volume):
    if tree_spp not in liquid_t:
        raise KeyError
    else:
        if volume < 0:
            raise ValueError
        else:
            add_list = {tree_spp: volume}
            tree_volume_list.append(add_list)
            return tree_volume_list


def reduce_tree_volume_list(tree_volume_list):
    new_dictionary = dict(functools.reduce(operator.add, map(collections.Counter, tree_volume_list)))
    return new_dictionary


def calculate_commercial_volume(new_dictionary):
    calculated_dictionary = {}
    if liquid_t.keys == new_dictionary.keys:
        calculated_volume = new_dictionary.values() * liquid_t.values() / 100
        calculated_dictionary.append
        return calculated_volume


# TODO pataisyti formule kad perskaiciuotu turi saraso zodyne pagal settings

def add_tree_volume(tree_spp, volume):
    if tree_spp not in liquid_t:
        raise KeyError
    else:
        if volume < 0:
            raise ValueError
        else:
            add_list = {tree_spp: volume}
            tree_volume_list.append(add_list)
            return tree_volume_list


# TODO irasytu i nauja sarasa zodyno rakta ir reiksmes apskaiciuota turi

def sum_volume_total():
    sum_lvol_total = round(fsum(tree_commercial_volume_list), 2)
    return sum_lvol_total


# TODO susumuoti tree_commercial_volume_list tūrius pagal medziu rusis

def sum_volume_total():
    sum_lvol_total = round(fsum(tree_commercial_volume_list), 2)
    return sum_lvol_total


# TODO funkcija kad susumuotu visa turi


def timber_price(average_price, preparation_price):
    t_price = round(average_price - preparation_price, 2)
    return t_price


def calculate_single_compensation():
    single_compensation = round(sum_list[0] * t_price, 2)
    return single_compensation


# TODO sum_list[0] pakeisti i kintamaji


def calculate_annual_compensation(interest):
    if interest > 0:
        annual_compensation = round(sum_list[0] * t_price * interest / 100, 2)
        return annual_compensation
    else:
        print(f'Kompensacija nemokama')


# TODO sum_list[0] pakeisti i kintamaji

test_list = [{'P': 100}, {'P': 100}, {'B': 100}, {'D': 100}]
new_dict = {'P': 200, 'B': 100, 'D': 100}
print(add_tree_volume('P', 100))
print(add_tree_volume('P', 100))
print(add_tree_volume('B', 100))
print(add_tree_volume('D', 100))
print(reduce_tree_volume_list(test_list))
print(calculate_commercial_volume(new_dict))
