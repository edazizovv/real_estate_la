#


#
import time
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

#


#
"""
d = './data/extended.csv'
data = pandas.read_csv(d).iloc[18:]

options = Options()
driver = webdriver.Firefox(options=options)

freeze_time = 0.5

listed = ['Ремонт', 'Транспортная доступность', 'Категория земель', 'Коммуникации', 'Этажей в доме', 'Материал стен', 'Количество комнат']
links = data['Ссылка'].values
results = []
for link in links:

    driver.get(link)

    time.sleep(freeze_time)

    res = {}
    for parameter in listed:

        try:
            elem = driver.find_element(By.XPATH, "//span[text()='{0}']".format(parameter))
            chick = elem.find_element(By.XPATH, "./..")

            res[parameter] = chick.text
        except NoSuchElementException:
            res[parameter] = 'NA'

    time.sleep(freeze_time)
    results.append(res)
"""

import ast

d = './data/mega.csv'
data = pandas.read_csv(d)
listed = ['Ремонт', 'Транспортная доступность', 'Категория земель', 'Коммуникации', 'Этажей в доме', 'Материал стен', 'Количество комнат']


data['pr'] = data['parsed'].apply(func=lambda x: ast.literal_eval(x)[listed[0]][8:])
data['pt'] = data['parsed'].apply(func=lambda x: ast.literal_eval(x)[listed[1]][26:])
data['pl'] = data['parsed'].apply(func=lambda x: ast.literal_eval(x)[listed[2]][18:])
data['pc'] = data['parsed'].apply(func=lambda x: ast.literal_eval(x)[listed[3]][14:])
data['ph'] = data['parsed'].apply(func=lambda x: ast.literal_eval(x)[listed[4]][15:])
data['pm'] = data['parsed'].apply(func=lambda x: ast.literal_eval(x)[listed[5]][15:])
data['pn'] = data['parsed'].apply(func=lambda x: ast.literal_eval(x)[listed[6]][19:])

data.to_csv(d, index=False)
