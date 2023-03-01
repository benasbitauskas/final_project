import methods

while True:
    pasirinkimas = int(input(
        '1 - Įvesti pajamas, siunėją, pastabas \n2 - Įvesti išlaidas, siuntimo būdą, kas įsigyta \n3 - Gauti balansą \n4 - parodyti ataskaitą \n9 - išeiti iš programos\n'))
    if pasirinkimas == 1:
        suma = float(input('Įveskite pajamų sumą: '))
        siuntejas = input('Įveskite siuntėją: ')
        pastabos = input('Įveskite pastabas: ')
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, pastabos)
    if pasirinkimas == 2:
        suma = float(input('Įveskite išlaidų sumą: '))
        atsiskaitymas = input('Įveskite atsiskaitymo būdą: ')
        isigyta = input('Įveskite įsigytą prekę/paslaugą: ')
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymas, isigyta)
    if pasirinkimas == 3:
        print(f'Balansas: {biudzetas.gauti_balansą()}')
    if pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
    if pasirinkimas == 9:
        print('Programa baigta')
        break


