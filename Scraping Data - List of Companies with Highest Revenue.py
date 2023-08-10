#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


print(soup)


soup.find('table', class_ = 'wikitable sortable')


soup.find('table')


<table class="wikitable sortable jquery-tablesorter">
<caption>


table = soup.find_all('table')[1]
table()


world_titles = table.find_all('th')
world_titles


world_table_titles = [titles.text.strip() for titles in world_titles]

print(world_table_titles)


import pandas as pd

df = pd.DataFrame(columns = world_table_titles)
df


columns_data = table.find_all('tr')

for row in columns_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data



df


df.to_csv(r'C:\Users\Arfan\Documents\Largest Companies\Companies.csv', index = False)
