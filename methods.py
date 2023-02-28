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


class Data:
    def __init__(self, tree_spp, volume):
        self.vol_dict = []
        self.sum_lvol_total = 0
        self.t_price = 0
        self.tree_spp = tree_spp
        self.volume = volume

    # apskaičiuoti paliekamą likvidinį tūrį pagal MR
    def calculate_lvolume(self):
        with open('dictionary_1.pkl', 'rb') as pickle_in:
            liquid_t = pickle.load(pickle_in)
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
        return round(self.sum_lvol_total, 2)

    # medienos kaina atėmus vidutines ruošos sąnaudas
    def timber_price(self, avg_price, prep_price):
        self.t_price = avg_price - prep_price
        return round(self.t_price, 2)

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
print(Data.sum_lvolume_total)
