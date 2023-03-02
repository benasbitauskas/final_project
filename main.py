from methods import *

plot = input('Įveskite sklypo kadastro Nr.: \n')
plotid = PlotInfo(plot)
plot_id_list.append(plot)

while True:
    try:
        choice = int(input(
            f'1 - Įvesti medžių rūšis ir tūrį \n2 - Skaičiuoti vienkartinę kompensaciją '
            f'\n3 - Skaičiuoti kasmetinę kompensaciją \n'
            f'9 - išeiti iš programos\n'))
    except ValueError:
        print('Neteisingas pasirinkimas')
        continue

    if choice == 1:
        tree_spp = input('Įveskite medžių rūšį: ')
        volume = float(input('Įveskite bendrą medienos tūrį: '))
        tree_volume = TreeSppVolume(tree_spp, volume)
        tree_volume._calculate_lvolume()
        tree_volume._sum_lvolume_total()

    elif choice == 2:
        avg_price = float(input('Įveskite vidutinę medienos kainą: '))
        prep_price = float(input('Įveskite vidutinę medienos ruošos kainą: '))
        single_compensation = TimberPriceCalculator(avg_price, prep_price)
        single_compensation.timber_price()
        print(f'Vienkartinė kompensacija: {single_compensation.calculate_single()} Eur')

    elif choice == 3:
        avg_price = float(input('Įveskite vidutinę medienos kainą: '))
        prep_price = float(input('Įveskite vidutinę medienos ruošos kainą: '))
        interest = float(input('Įveskite palūkanų normą: '))
        annual_compensation = TimberPriceCalculator(avg_price, prep_price, interest)
        annual_compensation.timber_price()
        print(f'Kasmetinė kompensacija: {annual_compensation.calculate_single()} Eur')

    elif choice == 9:
        print('Programa baigta')
        break
