import csv

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.baltpool.eu/medienos-birza/medienos-produktu-kainos/').text
soup = BeautifulSoup(source, 'html.parser')
block = soup.find('table', class_='bptbl timber_group_table')
# indexed_price = block.find('tr', class_='index-comp IN active')


with open('indeksuota_kaina.csv', 'w', encoding='UTF-8', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Data, kaina'])

    for info in block:
        try:
            indexed_price = info.find('tr', class_='index-comp IN active')
            csv_writer.writerow([indexed_price])
        except:
            pass
