# # Python code to demonstrate
# # return the sum of values of dictionary
# # with same keys in list of dictionary
#
# from operator import itemgetter
#
# # Initialising list of dictionary
# ini_dict = [{'a':5, 'b':10, 'c':90},
# 			{'a':45, 'b':78},
# 			{'a':90, 'c':10}]
#
# # printing initial dictionary
# print ("initial dictionary", str(ini_dict))
#
# # sum the values with same keys
# result = {}
# for d in ini_dict:
# 	for k in d.keys():
# 		result[k] = result.get(k, 0) + d[k]
#
#
# print("resultant dictionary : ", str(result))
#
#
# vol_dict = [{'P': 87.0}, {'P': 87.0}, {'D': 87.0}, {'B': 83.0}]
# print(str(vol_dict))
#
# def sum_lvolume_trees():
#     sumed_vol_dict = {}
#     for tree_spp in vol_dict:
#         for volume in tree_spp.keys():
#             sumed_vol_dict[volume] = sumed_vol_dict.get(volume, 0) + tree_spp[volume]
#     print(f'susumuoti {str(sumed_vol_dict)}')

# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.baltpool.eu/medienos-birza/medienos-produktu-kainos/'
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# table = soup.find('table', {'class': 'table table-bordered table-striped'})
# rows = table.find_all('tr')
#
# for row in rows:
#     cells = row.find_all('td')
#     if len(cells) > 0 and cells[0].get_text().strip() == 'Indeksas':
#         index_data = cells[1].get_text().strip()
#         print(f'Indeksas: {index_data}')

BASE_URL = 'https://www.baltpool.eu/medienos-birza/medienos-produktu-kainos/'
BASE_URL.format(row['prefix_1'], year, row['prefix_2'])

from settings import liquid_t


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


class Data:
    def __init__(self, tree_spp, volume):
        self.vol_dict = []
        self.sum_lvol_total = 0
        self.t_price = 0
        self.tree_spp = tree_spp
        self.volume = volume

    # apskaičiuoti paliekamą likvidinį tūrį pagal MR
    def calculate_lvolume(self):
        if self.tree_spp not in liquid_t:
            raise KeyError
        else:
            lvolume = self.volume * liquid_t[self.tree_spp] / 100
            if lvolume > 0:
                add_dict = {self.tree_spp: lvolume}
                self.vol_dict.append(add_dict)
                return round(lvolume, 2)
            else:
                raise ValueError

    # apskaičiuotas paliekamamas bendras likvidinis tūris
    def sum_lvolume_total(self):
        for volume in self.vol_dict:
            for tvolume in volume:
                self.sum_lvol_total += volume[tvolume]
        return self.sum_lvol_total



class Calculator(Data):
    # medienos kaina atėmus vidutines ruošos sąnaudas
    def timber_price(self, avg_price, prep_price):
        self.t_price = avg_price - prep_price
        return self.t_price

    # pajamos, kurios galėjo būti gautos pardavus medieną rinkoje, atimant iš jų
    # vidutines medienos ruošos sąnaudas, apskaičiuota vienkartinė kompensacija
    def calculate_single(self):
        value_single = self.sum_lvol_total * self.t_price
        return round(value_single, 2)

    # kompensuojami pajamų netekimo nuostoliai, apskaičiuojami kaip vidutinės metinės palūkanos,
    # mokamos einamaisiais metais Lietuvos komerciniuose bankuose už ilgalaikius (nuo 2 metų) terminuotus indėlius,
    # naujai priimtus iš ne finansų bendrovių ir namų ūkių
    # (jeigu nurodytos rūšies indėlių palūkanų norma einamaisiais metais
    # Lietuvos komerciniuose bankuose yra neigiama, kompensacija nemokama).
    # Palūkanos apskaičiuojamos nuo negautų pajamų, kurios galėjo būti gautos iškirtus kirstinus medžius
    # ir pardavus medieną rinkoje, atimant iš jų vidutines medienos ruošos sąnaudas.

    def calculate_annual(self, interest):
        if interest <= 0:
            return f'Kompensacija nemokama'
        else:
            value_annual = self.sum_lvol_total * self.t_price * interest / 100
            return round(value_annual, 2)

trees_vol1 = Data('P', 100)
trees_vol2 = Data('D', 60.5)

print(trees_vol1.calculate_lvolume())
print(trees_vol2.calculate_lvolume())

# while True:
#     pasirinkimas = int(input(
#         '1 - Įvesti medžių rūšis: \n2 - Apskaičiuoti tūrį įvestų rūšių \n3 -  \n9 - išeiti iš programos\n'))
#     if pasirinkimas == 1:
#         tree_spp = input('Įveskite MR: ')
#         volume = float(input('Įveskite tūrį: '))
#         trees.tree_input(tree_spp, volume)
#         print('sekmingai prideta')
#     if pasirinkimas == 2:
#         print('Apskaičiuoti tūrį įvestų rūšių tūris:')
#         trees.sum_lvolume_total()
#     if pasirinkimas == 3:
#         print(f'Balansas:')
#     if pasirinkimas == 4:
#
#     if pasirinkimas == 9:
#         print('Programa baigta')
#         break

