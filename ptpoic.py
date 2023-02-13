'''Predicting the price of Iranian cars'''


import os
import pickle
import subprocess


dena_options = {'models': ['Turbo Plus', 'Normal', 'Plus'],
                'gearbox': ['Auto', 'Manual'],
                'colors': ['Gray', 'White', 'Black']}

p206_options = {'models': ['Style 2', 'Style 3 Panorama', 'Style 5'],
                'gearbox': ['Manual'],
                'colors': ['Blue', 'Gray', 'White', 'Black']}

p207_options = {'models': ['MC', 'Normal', 'Panorama', 'TU5', 'TU5 Panorama'],
                'gearbox': ['Auto', 'Manual'],
                'colors': ['White', 'Black']}

p405_options = {'models': ['GLX', 'GLX 2Fuel', 'SLX'],
                'gearbox': ['Manual'],
                'colors': ['Gray', 'White', 'Silver', 'Blacklead']}

ppars_options = {'models': ['ELX', 'LX', 'XU7', 'XU7P'],
                'gearbox': ['Manual'],
                'colors': ['Gray', 'White']}

pride_options = {'models': ['SE-111', 'SE-131', 'SE-151', 'Hatchback'],
                'gearbox': ['Manual'],
                'colors': ['White', 'Blacklead']}

quick_options = {'models': ['Normal'],
                'gearbox': ['Auto', 'Manual'],
                'colors': ['White', 'Black']}

saina_options = {'models': ['EX', 'S'],
                'gearbox': ['Manual'],
                'colors': ['White']}

samand_options = {'models': ['EF7-LX', 'EF7-LX 2Fuel', 'XU7-LX'],
                'gearbox': ['Manual'],
                'colors': ['Gray', 'White', 'Black']}

tiba_options = {'models': ['EX Hatchback', 'SX Hatchback'],
                'gearbox': ['Manual'],
                'colors': ['White']}

tondar_options = {'models': ['E2', 'Normal', 'Plus'],
                'gearbox': ['Auto', 'Manual'],
                'colors': ['White', 'Black']}


def print_head():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)
    print("[Predicting the price of Iranian cars]\n")


def main():
    print_head()

    print(' 1-Dena')
    print(' 2-Peugeot 206')
    print(' 3-Peugeot 207')
    print(' 4-Peugeot 405')
    print(' 5-Peugeot Pars')
    print(' 6-Pride')
    print(' 7-Quick')
    print(' 8-Saina')
    print(' 9-Samand')
    print('10-Tiba')
    print('11-Tondar90')

    car_name = input("\n[STEP 1] Please Select a car (1/11): ")

    cars = {'1': 'dena', '2': 'p206', '3': 'p207', '4': 'p405', '5': 'ppars', '6': 'pride',
            '7': 'quick', '8': 'saina', '9': 'samand', '10': 'tiba', '11': 'tondar90'}

    print_head()
    car_year = input("[STEP 2] Enter year of car production: ")

    print_head()
    car_km = input("[STEP 3] Enter the amount the car has moved in kilometers: ")


    if car_name == '1':
        cols = dena_options['models'] + dena_options['gearbox'] + dena_options['colors']
    elif car_name == '2':
        cols = p206_options['models'] + p206_options['gearbox'] + p206_options['colors']
    elif car_name == '3':
        cols = p207_options['models'] + p207_options['gearbox'] + p207_options['colors']
    elif car_name == '4':
        cols = p405_options['models'] + p405_options['gearbox'] + p405_options['colors']
    elif car_name == '5':
        cols = ppars_options['models'] + ppars_options['gearbox'] + ppars_options['colors']
    elif car_name == '6':
        cols = pride_options['models'] + pride_options['gearbox'] + pride_options['colors']
    elif car_name == '7':
        cols = quick_options['models'] + quick_options['gearbox'] + quick_options['colors']
    elif car_name == '8':
        cols = saina_options['models'] + saina_options['gearbox'] + saina_options['colors']
    elif car_name == '9':
        cols = samand_options['models'] + samand_options['gearbox'] + samand_options['colors']
    elif car_name == '10':
        cols = tiba_options['models'] + tiba_options['gearbox'] + tiba_options['colors']
    elif car_name == '11':
        cols = tondar_options['models'] + tondar_options['gearbox'] + tondar_options['colors']
    else:
        print('Wrong input!')

    print_head()
    print("[STEP 4] In order and separated by a space.\n         Enter 1 if correct, otherwise 0.\n")
    print(' | '.join(cols))

    car_details = input(">>> ").split()

    car_matrix = [car_year, car_km] + car_details
    car_matrix = list(map(int, car_matrix))

    model = pickle.load(open(f'models/{cars[car_name]}/{cars[car_name]}_model.sav', 'rb'))
    prediction = int(model.predict([car_matrix]))

    print_head()
    print(f'{prediction:,} T')


if __name__ == '__main__':
    main()