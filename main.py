from methods import *

# plot = input('Įveskite sklypo kadastro Nr.: \n')

avg_price = 0
prep_price = 0

data = Data()

while True:
    try:
        choice = int(input(
            f'1 - Įvesti medžių rūšis ir tūrį \n'
            f'2 - Apskačiuoti likvidinį tūri \n'
            f'3 - Apskaičiuoti medienos kainą \n'
            f'4 - Skaičiuoti vienkartinę kompensaciją \n'
            f'5 - Skaičiuoti kasmetinę kompensaciją \n'
            f'6 - Atakskaita \n'
            f'9 - išeiti iš programos\n'))
    except ValueError:
        print('Neteisingas pasirinkimas')
        continue

    if choice == 1:
        tree_spp = input('Įveskite medžių rūšį: ')
        volume = float(input('Įveskite bendrą medienos tūrį: '))
        tree_volume = add_tree_volume(tree_spp, volume)

    elif choice == 2:
        print(f'Likvidinis tūris {calculate_commercial_volume()}')

    elif choice == 3:
        avg_price = float(input('Įveskite vidutinę medienos kainą: '))
        prep_price = float(input('Įveskite vidutinę medienos ruošos kainą: '))
        timber_price = calculate_timber_price(avg_price, prep_price)
        print(f'Medienos kaina: {timber_price} Eur')

    elif choice == 4:
        single_compensation = calculate_single_compensation(avg_price, prep_price)
        print(f'Vienkartinė kompensacija: {single_compensation} Eur')

    elif choice == 5:
        interest = float(input('Įveskite palūkanų normą: '))
        annual_compensation = calculate_annual_compensation(interest, avg_price, prep_price)
        print(f'Kasmetinė kompensacija: {annual_compensation} Eur')

    elif choice == 6:
        data.add_data(tree_volume, timber_price, single_compensation, annual_compensation)
        #TODO FIX
    elif choice == 9:
        print('Programa baigta')
        break
