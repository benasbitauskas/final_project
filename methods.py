from settings import liquid_t
from math import fsum


class PlotInfo:
    """
    įvesti sklypo duomenys: kadastro Nr.
    """

    def __init__(self, plot_id):
        self.plot_id = plot_id


class TreeSppVolume:

    def __init__(self, tree_spp, volume):
        self.tree_spp = tree_spp
        self.volume = volume

    #
    def _calculate_lvolume(self):
        """
        apskaičiuoti paliekamą likvidinį tūrį pagal MR
        """
        if self.tree_spp not in liquid_t:
            raise KeyError
        else:
            lvolume = self.volume * liquid_t[self.tree_spp] / 100
            if lvolume > 0:
                add_list = round(lvolume, 2)
                vol_list.append(add_list)
                return add_list
            else:
                raise ValueError

    def _sum_lvolume_total(self):
        """
        apskaičiuotas paliekamamas bendras likvidinis tūris
        """
        sum_lvol_total = fsum(vol_list)
        return round(sum_lvol_total, 2)

    def process_data(self):
        lvolume = self._calculate_lvolume()
        # TODO lvolume išsaugoti į DB
        return self._sum_lvolume_total()


class TimberPriceCalculator:
    def __init__(self, avg_price, prep_price, interest=0.0):
        self.avg_price = avg_price
        self.prep_price = prep_price
        self.interest = interest
        self.t_price = 0

    def timber_price(self):
        """
        medienos kaina atėmus vidutines ruošos sąnaudas
        """
        self.t_price = round(self.avg_price - self.prep_price, 2)
        return self.t_price

    def calculate_single(self):
        """
        pajamos, kurios galėjo būti gautos pardavus medieną rinkoje, atimant iš jų
        vidutines medienos ruošos sąnaudas, apskaičiuota vienkartinė kompensacija
        """
        return round(sum_lvol_total * self.t_price, 2)

    def calculate_annual(self):
        """
        jeigu nurodytos rūšies  palūkanos neigiama, kompensacija nemokama.
        Palūkanos apskaičiuojamos nuo negautų pajamos kurios galėjo būti gautos
        pardavus medieną rinkoje, atimant iš jų vidutines medienos ruošos sąnaudas.
        """
        if self.interest <= 0:
            compensation = f'Kompensacija nemokama'
        else:
            compensation = round(sum_lvol_total * self.t_price * self.interest / 100, 2)
        return compensation

    # def process_data(self, calculate_type):
    #     if calculate_type == 'single':
    #         price = self.calculate_single()
    #     elif calculate_type == 'annual':
    #         price = self.calculate_annual()
    #     else:
    #         raise ValueError('')  # TODO užpildyti error paaiškinimą kad nėra tokio pasirinkimo
    #     return price


plot_id_list = []
vol_list = []
plot = input('Įveskite sklypo kadastro Nr.:')
plotid = PlotInfo(plot)
plot_id_list.append(plot)
print(plot_id_list)

# timber_price = TimberPriceCalculator(70.69, 13.90)
# trees_vol1 = TreeSppVolume('P', 100)
# trees_vol2 = TreeSppVolume('D', 60.5)
# sum_lvol_total = trees_vol1.process_data() + trees_vol2.process_data()


# while True:
#     pasirinkimas = int(input(
#         '1 - Įvesti pajamas, siunėją, pastabas \n2 - Įvesti išlaidas, siuntimo būdą, kas įsigyta \n3 - Gauti balansą \n4 - parodyti ataskaitą \n9 - išeiti iš programos\n'))
#     if pasirinkimas == 1:
#         suma = float(input('Įveskite pajamų sumą: '))
#         siuntejas = input('Įveskite siuntėją: ')
#         pastabos = input('Įveskite pastabas: ')
#         biudzetas.prideti_pajamu_irasa(suma, siuntejas, pastabos)
#     if pasirinkimas == 2:
#         suma = float(input('Įveskite išlaidų sumą: '))
#         atsiskaitymas = input('Įveskite atsiskaitymo būdą: ')
#         isigyta = input('Įveskite įsigytą prekę/paslaugą: ')
#         biudzetas.prideti_islaidu_irasa(suma, atsiskaitymas, isigyta)
#     if pasirinkimas == 3:
#         print(f'Balansas: {biudzetas.gauti_balansą()}')
#     if pasirinkimas == 4:
#         biudzetas.parodyti_ataskaita()
#     if pasirinkimas == 9:
#         print('Programa baigta')
#         break


# price = timber_price.process_data(calculate_type='')
