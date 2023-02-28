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
        self.tree_spp = tree_spp
        self.volume = volume
        self.sum_lvol_total = 0
        self.tree_dict = []
        self.vol_dict = []
        self.t_price = 0

    def add_tree(self):
        with open('../dictionary_1.pkl', 'rb') as pickle_in:
            liquid_t = pickle.load(pickle_in)
        if self.tree_spp not in liquid_t:
            raise KeyError
        else:
            if self.volume < 0:
                raise ValueError
            else:
                add_dict = Data(self.tree_spp, self.volume)
                self.tree_dict.append(add_dict)
                return self.tree_dict


    # apskaičiuoti paliekamą likvidinį tūrį pagal MR
    def calculate_lvolume(self):
        lvolume = volume * liquid_t[tree_spp] / 100
        add_dict = {tree_spp: lvolume}
        self.vol_dict.append(add_dict)
        return round(lvolume, 2)

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

print(trees_vol1.add_tree())
print(trees_vol2.add_tree())
