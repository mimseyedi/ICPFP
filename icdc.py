'''Iranian cars data collector'''

import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd


def collecting_data(links: list) -> list:
    cars_data = []
    driver = webdriver.Safari()
    case = 1

    for link in links:
        try:
            sys.stdout.write(f'\033[92mBrowsing case {case}. Please wait...\n')
            driver.get(link)

            time.sleep(5)
            for _ in range(4):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)

            soap = BeautifulSoup(driver.page_source, 'html.parser')

            cars_card = soap.find_all('a', class_='bama-ad', href=True)

            progress = 1
            for cars in cars_card:
                sys.stdout.write(f'\033[92mcase [{case}/{len(links)}] - item [{progress}/{len(cars_card)}]\n')
                sys.stdout.flush()

                response = requests.get(f"https://bama.ir{cars['href']}")
                detail_soup = BeautifulSoup(response.text, 'html.parser')

                car, model = [], ''

                for name in detail_soup.find_all('h1', class_='bama-ad-detail-title__title'):
                    name = name.text.split()
                    if len(name) > 1:
                        car.append(name[0])
                        model = name[1]
                    else:
                        car.append(name[0])

                for detail in detail_soup.find_all('span', class_='bama-ad-detail-title__subtitle'):
                    car.append(detail.text.strip())

                try:
                    car[-1] += f'-{model}'
                except IndexError: ...

                counter = 0
                for detail in detail_soup.find_all('div', class_='bama-vehicle-detail-with-icon__detail-holder'):
                    if counter in [0, 2, 3]:
                        car.append(detail.text.strip())
                    counter += 1

                for price in detail_soup.find_all('span', class_='bama-ad-detail-price__price-text'):
                    car.append(price.text.strip())

                cars_data.append(car)
                progress += 1

            case += 1

        except requests.exceptions.ConnectionError: ...

    return cars_data


def save_to_csv(csv_path: str, data: list) -> bool:
    data_frame = pd.DataFrame(data)
    data_frame.to_csv(csv_path, index=False, encoding='utf-8')


def main():
    links = ['https://bama.ir/car/pride?priced=1&status=no_paint&country=iranian',
             'https://bama.ir/car/peugeot-206ir?priced=1&status=no_paint&country=iranian',
             'https://bama.ir/car/peugeot-pars?priced=1&status=no_paint&country=iranian',
             'https://bama.ir/car/peugeot-405?priced=1&status=no_paint&country=iranian',
             'https://bama.ir/car/peugeot-207?priced=1&status=no_paint&country=iranian',
             'https://bama.ir/car/tiba?priced=1&status=no_paint&country=iranian',
             'https://bama.ir/car/dena?priced=1&status=no_paint&country=iranian',
             'https://bama.ir/car/quick?priced=1&status=no_paint&country=iranian',
             'https://bama.ir/car/samand?priced=1&status=no_paint&country=iranian',
             'https://bama.ir/car/saina?priced=1&status=no_paint&country=iranian',
             'https://bama.ir/car/renault-tondar90?priced=1&status=no_paint&country=iranian']

    cars_data = collecting_data(links=links)
    save_to_csv('dataset.csv', cars_data)
    print('\033[92m\n[--------PROCESS COMPLETED--------]\033[0m')


if __name__ == '__main__':
    main()