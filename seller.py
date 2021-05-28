from typing import List, Any

import requests

from bs4 import BeautifulSoup

import csv

import time

import re

begin = time.time()

url_list = []

all_elements = []


def read_oxi():
    filename = open('outputv15.csv', 'r')

    file = csv.DictReader(filename, delimiter=',')

    for col in file:
        url_list.append(col['Product_url'])


read_oxi()


def get_seller_rating(soup):
    try:
        seller_string = soup.find('div', attrs={'class': '_3LWZlK _1D-8OL'}).text.strip()

        def convert(string):
            list1 = []
            list1[:0] = string
            return list1

        my_list = convert(seller_string)

        print(my_list)

        if '.' in my_list:

            seller_rating = my_list[-3] + '.' + my_list[-1]

            print(f"the seller_rating is a float {seller_rating}")

        else:

            seller_rating = my_list[-1]
            print(f" the seller_rating is integer {seller_rating}")


    except AttributeError:
        number = 0
        print(f"the rating is {number}")


def parse_data():
    for url in url_list:

        print(url)

        new_page = requests.get(url)

        if new_page.status_code == 200:

            count = count + 1

            print(f"The count od the list is {count}")

            new_soup = BeautifulSoup(new_page.text, 'lxml')

            seller_rating_data = get_seller_rating(new_soup)

            all_elements.append(  # saving all elements to a list
                {
                    "Product_url": url,
                    "Seller_rating_Data": seller_rating_data

                })

            keys = all_elements[0].keys()

            with open('seller2.csv', 'w', newline='') as output_file:  # writing all elements to csv
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(all_elements)



        else:
            pass


parse_data()

print(len(all_elements))

end = time.time()
print(f"Total runtime of the program is {end - begin}")
