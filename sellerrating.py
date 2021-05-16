import difflib

import requests

from bs4 import BeautifulSoup

import csv

import re

import time

begin = time.time()

url_list = ["https://www.flipkart.com/trendzie-care-pulse-oximeter-finger-tip-blood-oxygen-saturation-monitor-rate-pr-oled-digital-display-oximeter/p/itm8316aec83d1e5?pid=POXG2XT8CAWE6BBP",
            "https://www.flipkart.com/co-healthy-pu1-pulse-oximeter/p/itm90e0ec8da40fc?pid=POXFVPTGKBBMNFHR",
            "https://www.flipkart.com/lk87-lk87001-pulse-oximeter/p/itm227d8d3057279?pid=POXG2VE3RPWZNYPM",
            "https://www.flipkart.com/jo-pharma-100-oximeter-premium-pulse/p/itmdf92bb6cd2aee?pid=POXG2QWXECSQBF3T"]






def get_seller_rating(soup):

    try:
        seller_name_string = soup.find('div', id="sellerName").text.strip()

        try:

            seller_name = seller_name_string.replace('.', '')



            print(seller_name)

        except Exception as e:

            seller_name = "Not available"
            print(seller_name)

    except AttributeError:

        seller_name = "Not available"
        print(seller_name)

    return seller_name

    return seller_rating

def get_seller_name(soup):

    try:
        seller_name_string = soup.find('div', id="sellerName").text.strip()


        try:

            seller_name = seller_name_string.replace('.', '')

            seller_name = ''.join([i for i in seller_name if not i.isdigit()])

            print(seller_name)

        except Exception as e:

            seller_name = "Not available"
            print(seller_name)

    except AttributeError:

        seller_name = "Not available"
        print(seller_name)


    return seller_name

def parse_data():

        for url in url_list:

            print(url)

            new_page = requests.get(url)

            if new_page.status_code == 200:



                new_soup = BeautifulSoup(new_page.text, 'lxml')

                seller_rating_data = get_seller_rating(new_soup)
                seller_name = get_seller_name(new_soup)


            else:
                pass



parse_data()
end = time.time()
print(f"Total runtime of the program is {end - begin}")