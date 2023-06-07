#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://proxyway.com/news"

# Menyiapkan file CSV
csv_file = open('scraping_results.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Page', 'Title', 'Date'])

page = 1
while True:
    page_url = URL + '/page/' + str(page)
    req = requests.get(page_url)
    soup = bs(req.text, 'html.parser')
    articles = soup.find_all('div', class_='archive-list__wrap')

    if not articles:
        break

    for article in articles:
        title = article.find('h3', class_='archive-list__title').text.strip()
        date = article.find('span', class_='archive-list__date').text.strip()
        csv_writer.writerow([page, title, date])

    page += 1

# Menutup file CSV
csv_file.close()

print("Data telah disimpan dengan nama 'scraping_results.csv'")


# In[ ]:




