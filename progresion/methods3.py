import pickle

# sklypo savininko duomenys
# class Credentials:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
# įvesti sklypo duomenys: kadastro Nr., savivaldybė, seniūnyja, kaimas
# class Plot_info:
#     def __init__(self, plot_id, municipality, eldership, village):
#         self.plot_id = plot_id
#         self.municipality = municipality
#         self.eldership = eldership
#         self.village = village


tree_dict = []
vol_dict = []
t_price = 0
sum_lvol_total = 0

def add_tree(tree_spp, volume):
    with open('../dictionary_1.pkl', 'r') as pickle_in:
        liquid_t = pickle.load(pickle_in)
    if tree_spp not in liquid_t:
        raise KeyError
    else:

        if volume < 0:
            raise ValueError
        else:
            lvolume = volume * liquid_t[tree_spp] / 100
            add_dict = {tree_spp: volume}
            add_vol = {tree_spp: lvolume}
            vol_dict.append(add_vol)
            tree_dict.append(add_dict)
            return tree_dict, vol_dict


# apskaičiuotas paliekamamas bendras likvidinis tūris
def sum_lvolume_total():

    for volume in vol_dict:
        for tvolume in volume:
            sum_lvol_total += volume[tvolume]
    return round(sum_lvol_total, 2)


# medienos kaina atėmus vidutines ruošos sąnaudas
def timber_price(avg_price, prep_price):
    t_price = avg_price - prep_price
    return round(t_price, 2)


# pajamos, kurios galėjo būti gautos pardavus medieną rinkoje, atimant iš jų
# vidutines medienos ruošos sąnaudas, apskaičiuota vienkartinė kompensacija
def calculate_single():
    value_single = sum_lvol_total * t_price
    return round(value_single, 2)


# kompensuojami pajamų netekimo nuostoliai, apskaičiuojami kaip vidutinės metinės palūkanos,
# mokamos einamaisiais metais Lietuvos komerciniuose bankuose už ilgalaikius (nuo 2 metų) terminuotus indėlius,
# naujai priimtus iš ne finansų bendrovių ir namų ūkių
# (jeigu nurodytos rūšies indėlių palūkanų norma einamaisiais metais
# Lietuvos komerciniuose bankuose yra neigiama, kompensacija nemokama).
# Palūkanos apskaičiuojamos nuo negautų pajamų, kurios galėjo būti gautos iškirtus kirstinus medžius
# ir pardavus medieną rinkoje, atimant iš jų vidutines medienos ruošos sąnaudas.

def calculate_annual(interest):
    if interest <= 0:
        return f'Kompensacija nemokama'
    else:
        value_annual = sum_lvol_total * t_price * interest / 100
        return round(value_annual, 2)


spp1 = 'P'
spp2 = 'B'
vol1 = 100
vol2 = 100
prep = 13.90
price = 70.69
interest = 2.06

print(add_tree(spp1, vol1))
print(add_tree(spp2, vol2))
print(sum_lvolume_total())
