from settings import liquid_t
import collections
import functools
import operator
import logs as lg

tree_volume_list = []


# 1
def add_tree_volume(tree_spp, volume):
    if tree_spp not in liquid_t:
        lg.logger.exception('Žodyne nėra nurodytos MR')
        raise KeyError
    else:
        if volume < 0:
            lg.logger.exception(f'Įvestas tūris negali būti neigiamas {lvolume}')
            raise ValueError
        else:
            add_list = {tree_spp: volume}
            tree_volume_list.append(add_list)
            lg.logger.info(f'Pridėtos MR ir tūris į sąrašą {tree_volume_list}')
            return tree_volume_list


# 2
def reduce_tree_volume_list():
    new_dictionary = dict(functools.reduce(operator.add, map(collections.Counter, tree_volume_list)))
    lg.logger.info(f'Susumuotos vienodų MR žodynas {new_dictionary}')
    return new_dictionary
    # 3


def sum_volume_total():
    new_dictionary = reduce_tree_volume_list()
    volume_total = sum(new_dictionary.values())
    lg.logger.info(f'Bendras tūris {volume_total}')
    return volume_total


# 4
def calculate_commercial_volume():
    new_dictionary = reduce_tree_volume_list()
    calculated_cvolume = {key: new_dictionary[key] * liquid_t[key] / 100 for key in new_dictionary}
    lg.logger.info(f'Apskaičiuotas likvidinis tūris {calculated_cvolume}')
    return calculated_cvolume


# 5
def sum_cvolume_total():
    calculated_cvolume = calculate_commercial_volume()
    cvolume_sum = sum(calculated_cvolume.values())
    lg.logger.info(f'apskaičiuotas bendras paliekamas likvidinis tūris{cvolume_sum}')
    return cvolume_sum


# 6
def timber_price(average_price, preparation_price):
    t_price = round(average_price - preparation_price, 2)
    lg.logger.info(f'medienos kaina atėmus vidutines ruošos sąnaudas {t_price}')
    return t_price


# 7
def calculate_single_compensation():
    cvolume_sum = sum_cvolume_total()
    t_price = timber_price()
    single_compensation = round(cvolume_sum * t_price, 2)
    lg.logger.info(f'Apskaičiuota vienakartinė kompensacija {single_compensation}')
    return single_compensation  # TODO fix


# 8
def calculate_annual_compensation(lvolume_sum, t_price, interest):
    if interest > 0:
        annual_compensation = round(lvolume_sum * t_price * interest / 100, 2)
        lg.logger.info(f'Apskaičiuota kasmetinė kompensacija {annual_compensation}')
        return annual_compensation  # TODO fix
    else:
        lg.logger.info(f'Kompensacija nemokama')
        return f'Kompensacija nemokama'


# test_list = [{'P': 100}, {'P': 100}, {'B': 100}, {'D': 100}]
# new_dict = {'P': 200, 'B': 100, 'D': 100}
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
print(f'3: {sum_volume_total()}')
print(f'4: {calculate_commercial_volume()}')
print(f'5: {sum_cvolume_total()}')
print(f'6: {timber_price(average_price, preparation_price)}')
print(f'7: {calculate_single_compensation()}')
print(f'8: {calculate_annual_compensation(average_price, preparation_price, interest)}')
