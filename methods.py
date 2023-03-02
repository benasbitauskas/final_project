from settings import liquid_t
from math import fsum
import logs as lg


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
        if self.tree_spp not in liquid_t:
            lg.logger.info(f'Įvesto medžio rūšies nėra žodyne {self.tree_spp}')
            raise KeyError
        else:
            lvolume = self.volume * liquid_t[self.tree_spp] / 100
            if lvolume > 0:
                add_list = round(lvolume, 2)
                vol_list.append(add_list)
                lg.logger.info(f'Apskaičiuotas medžio rūšies tūris {lvolume}')
                return lvolume
            else:
                lg.logger.info(f'Įvestas tūris negali būti neigiamas {lvolume}')
                raise ValueError

    @staticmethod
    def _sum_lvolume_total():
        sum_lvol_total = round(fsum(vol_list), 2)
        sum_list[0] = sum_lvol_total
        lg.logger.info(f'Apskaičiuotas bendras paliekamas likvidinis tūris {sum_list[0]}')
        return sum_list[0]


class TimberPriceCalculator:
    def __init__(self, avg_price, prep_price, interest=0.0):
        self.avg_price = avg_price
        self.prep_price = prep_price
        self.interest = interest
        self.t_price = 0

    def timber_price(self):
        self.t_price = round(self.avg_price - self.prep_price, 2)
        lg.logger.info(f'Medienos kaina atėmus vidutines ruošos sąnaudas {self.t_price}')
        return self.t_price

    def calculate_single(self):
        single = round(sum_list[0] * self.t_price, 2)
        lg.logger.info(f'Apskaičiuota vienkartinė kompensacija {single}')
        return single

    def calculate_annual(self):
        if self.interest > 0:
            annual = round(sum_list[0] * self.t_price * self.interest / 100, 2)
            lg.logger.info(f'Kasmetinė kompensacija {annual}')
            return annual

        else:
            lg.logger.info(f'Palūkanų norma 0 arba neigiama {self.interest}')
            print(f'Kompensacija nemokama')


sum_list = [0.0]
plot_id_list = []
vol_list = []
