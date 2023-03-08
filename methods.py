from settings import liquid_t
import collections
import functools
import operator
import logs as lg

tree_volume_list = []


def capitalize_input_tree_spp(tree_spp):
    if not isinstance(tree_spp, str):
        lg.logger.exception('Įvesta MR ne string')
        raise ValueError
    else:
        tree_spp = tree_spp.upper()
        lg.logger.info(f'Pakeista MR {tree_spp}')
        return tree_spp


def add_tree_volume(tree_spp, volume):
    lvolume = 0
    tree_spp = capitalize_input_tree_spp(tree_spp)
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


def reduce_tree_volume_list():
    new_dictionary = dict(functools.reduce(operator.add, map(collections.Counter, tree_volume_list)))
    lg.logger.info(f'Susumuotos vienodų MR žodynas {new_dictionary}')
    return new_dictionary


def sum_volume():
    new_dictionary = reduce_tree_volume_list()
    volume_total = sum(new_dictionary.values())
    lg.logger.info(f'Bendras tūris {volume_total}')
    return volume_total


def calculate_commercial_volume():
    new_dictionary = reduce_tree_volume_list()
    calculated_cvolume = {key: new_dictionary[key] * liquid_t[key] / 100 for key in new_dictionary}
    lg.logger.info(f'Apskaičiuotas likvidinis tūris {calculated_cvolume}')
    return calculated_cvolume


# 5
def sum_cvolume_total():
    calculated_cvolume = calculate_commercial_volume()
    cvolume_sum = sum(calculated_cvolume.values())
    lg.logger.info(f'Apskaičiuotas bendras paliekamas likvidinis tūris {cvolume_sum}')
    return cvolume_sum


def calculate_timber_price(average_price, preparation_price):
    t_price = round(average_price - preparation_price, 2)
    lg.logger.info(f'Medienos kaina atėmus vidutines ruošos sąnaudas {t_price}')
    return t_price


def calculate_single_compensation(average_price, preparation_price):
    t_price = calculate_timber_price(average_price, preparation_price)
    cvolume_sum = sum_cvolume_total()
    single_compensation = round(cvolume_sum * t_price, 2)
    lg.logger.info(f'Apskaičiuota vienakartinė kompensacija {single_compensation}')
    return single_compensation  # TODO fix


def calculate_annual_compensation(interest, average_price, preparation_price):
    t_price = calculate_timber_price(average_price, preparation_price)
    cvolume_sum = sum_cvolume_total()
    if interest > 0:
        annual_compensation = round(cvolume_sum * t_price * interest / 100, 2)
        lg.logger.info(f'Apskaičiuota kasmetinė kompensacija {annual_compensation}')
        return annual_compensation
    else:
        lg.logger.info(f'Kompensacija nemokama')
        return f'Kompensacija nemokama'
