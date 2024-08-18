#


#
import pandas
import seaborn
from sklearn.preprocessing import KBinsDiscretizer
from matplotlib import pyplot

#


#
d = './data/data.csv'
data = pandas.read_csv(d)

import requests
import urllib.parse

TOKEN = ''  # yandex maps token

# url = 'https://nominatim.openstreetmap.org/search?q=' + urllib.parse.quote(address) +'?format=json'
# def treater(x):
#     return x.replace('ул. ', '').replace('ул.', '').replace(',', '').replace('.', '').replace('р-н ', '')
# data['preproc_address'] = data['Адрес'].apply(func=treater)


def get_l1l2(x):
    if x == '-':
        return 'NA NA'
    else:
        url = 'https://geocode-maps.yandex.ru/1.x?apikey={0}&geocode={1}&format=json'.format(TOKEN,
                                                                                             urllib.parse.quote(x))
        response = requests.get(url).json()
        return response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']


def get_l1(x):
    l1, l2 = x.split(' ')
    return l1


def get_l2(x):
    l1, l2 = x.split(' ')
    return l2


data['l1l2'] = data['Адрес'].apply(func=get_l1l2)
data['l1'] = data['l1l2'].apply(func=get_l1)
data['l2'] = data['l1l2'].apply(func=get_l2)

data.to_csv('./data/extended.csv', index=False)
