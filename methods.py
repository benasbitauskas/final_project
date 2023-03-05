from settings import liquid_t
# from math import fsum
import collections
import functools
import operator


# import logs as lg

# 1
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


# 2
def reduce_tree_volume_list():
    new_dictionary = dict(functools.reduce(operator.add, map(collections.Counter, tree_volume_list)))
    return new_dictionary


# 3
def sum_volume_total():
    return sum(new_dictionary.values())
#TODO fix

# 4
def calculate_commercial_volume(new_dictionary):
    calculated_lvolume = {key: new_dictionary[key] * liquid_t[key] / 100 for key in new_dictionary}
    return calculated_lvolume


# 5
def sum_lvolume_total(calculated_lvolume):
    lvolume_sum = sum(calculated_lvolume.values())
    return lvolume_sum


# 6
def timber_price(average_price, preparation_price):
    t_price = round(average_price - preparation_price, 2)
    return t_price


# 7
def calculate_single_compensation(t_price, lvolume_sum):
    single_compensation = round(lvolume_sum * t_price, 2)
    return single_compensation


# 8
def calculate_annual_compensation(lvolume_sum, t_price, interest):
    if interest > 0:
        annual_compensation = round(lvolume_sum * t_price * interest / 100, 2)
        return annual_compensation
    else:
        return f'Kompensacija nemokama'


tree_volume_list = []
tree_commercial_volume_list = []
test_list = [{'P': 100}, {'P': 100}, {'B': 100}, {'D': 100}]
new_dict = {'P': 200, 'B': 100, 'D': 100}
average_price = 70.69
preparation_price = 13.90
lvolume = {'P': 174.0, 'B': 83.0, 'D': 87.0}
lvolume_total = 344
t_price = 56.79
interest = 2.06
print(add_tree_volume('P', 100))
print(add_tree_volume('P', 100))
print(add_tree_volume('B', 100))
print(add_tree_volume('D', 100))
print(f'2: {reduce_tree_volume_list()}')
print(f'3: {sum_volume_total(new_dict)}')
print(f'4: {calculate_commercial_volume(new_dict)}')
print(f'5: {sum_lvolume_total(lvolume)}')
print(f'6: {timber_price(average_price, preparation_price)}')
print(f'7: {calculate_single_compensation(t_price, lvolume_total)}')
print(f'8: {calculate_annual_compensation(t_price, lvolume_total, interest)}')
