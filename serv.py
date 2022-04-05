import json
from bs4 import BeautifulSoup
import requests

url = 'https://blsspain-belarus.com/contact.php'

def get_info_site(url: str):
    r = requests.get(url)
    return r.text


def collect_info_data(html):
    all_centres = []

    soup = BeautifulSoup(html, 'lxml')

    centers = soup.find_all('table', class_='table')

    for center in centers:

        info = {}

        country_and_type = center.find('th')
        if country_and_type is None:
            break
        country_and_type = country_and_type.text.split(' ')

        info["Страна"] = country_and_type[0]
        info["Тип"] = country_and_type[1] + ' ' + country_and_type[2]

        parts = center.find_all('div', class_='marginBottom')

        for part in parts:
            rows = part.find_all('div', class_='row')
            if (rows[0].text == "Часы работы:"):
                info[rows[0].text[:-1:]] = {rows[1].text: rows[2].text,
                                            rows[3].text: rows[4].text}

            elif (rows[0].text == "Адрес"):
                address = rows[1].text.replace('\n\t', '').split(', ')
                info["Город"] = address[0]
                info["Адрес"] = address[2][:-1:] + ', ' + address[3]

            else:
                info[rows[0].text] = rows[1].text

        all_centres.append(info)

    return all_centres

def visa_center_to_file(all_centres):
    with open("data_spain.json", "w", encoding="utf-8") as file:
        json.dump(all_centres, file, ensure_ascii=False)

def read_visa_center():
    with open("data_spain.json", "r", encoding="utf-8") as file:
        text = json.load(file)
    return text

def create_file():
    html = get_info_site(url)
    all_centres = collect_info_data(html)
    visa_center_to_file(all_centres)
    return all_centres



