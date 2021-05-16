import requests

from bs4 import BeautifulSoup

import re

import csv

base_url = "https://www.flipkart.com/search?q=washing+machine&page="

pagination_urls = []  # the products are listed in n mumber of pages and the urls to be stored in this list

product_urls = []# the urls to individual products

all_elements = []

cleaned_product_ulrs = []

def generate_page_url():  # function to generate the pagination urls and save it to the list pagination urls

    count = 0

    while count < 32:
        page_url = base_url + str(count) #generating the url

        print(page_url)

        pagination_urls.append(page_url) #append to the list pagination urls

        print(count)

        count = count + 1

generate_page_url()

def generate_product_page_url():

    for page in pagination_urls:

        response = requests.get(page)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'lxml')

            for link in soup.find_all('a', attrs={'class': '_1fQZEK'}):
                item_url = " https://www.flipkart.com" + link.get('href')

                item_url = re.split("\&", item_url)

                item_url = item_url[0]

                print(item_url)

                product_urls.append(item_url)

                print(len(product_urls))

generate_product_page_url()

def remove_duplicates():

    for i in product_urls:
        if i not in cleaned_product_ulrs:
            cleaned_product_ulrs.append(i)

    print(len(cleaned_product_ulrs))

remove_duplicates()


