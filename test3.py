import requests

from bs4 import BeautifulSoup

import csv

import time

import re

begin = time.time()

url_list = []

all_elements = []


def get_star_rating(soup):
    try:

        star_rating = soup.find('div', attrs={'class': '_2d4LTz'}).text.strip()
        print(f" the star_rating is {star_rating}")

    except AttributeError:

        star_rating = "0"
        print(f" the star_rating is {star_rating}")

    return star_rating


def read_oxi():
    filename = open('outputv15.csv', 'r')

    file = csv.DictReader(filename, delimiter=';')

    for col in file:
        url_list.append(col['Product_url'])


read_oxi()


def get_product_ratings(soup):
    try:
        number_of_ratings = soup.find('span', attrs={'class': '_2_R_DZ'}).text
        try:
            temp = number_of_ratings.split()
            ratings = temp[0].strip()
            ratings = ratings.replace(',', '')
            print(f" the ratings are {ratings}")
        except IndexError:
            ratings = "0"
    except AttributeError:
        ratings = "0"

    return ratings


def get_seller_rating(soup):
    try:
        seller_rating_string = soup.find('div', id="sellerName").text.strip()

        # seller_name = re.split("[0-9]", seller_name)

        temp = re.findall(r'\d+', seller_rating_string)
        seller_rating_temp = list(map(int, temp))

        if (len(seller_rating_temp)) == 1:

            seller_rating = seller_rating_temp[0]

            print(f"The seller rating is {seller_rating}")

        elif (len(seller_rating_temp)) >= 2:



            var1 = seller_rating_temp[-1]
            var2 = seller_rating_temp[-2]

            seller_rating = float(str(var2) + "." + str(var1))
            print(f"The seller rating is {seller_rating}")
        else:
            seller_rating = "0"
            print(f"The seller rating is {seller_rating}")


    except AttributeError:

        seller_rating = "Name Not available"

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


def get_reviews(soup):
    try:
        number_of_reviews = soup.find('span', attrs={'class': '_2_R_DZ'}).text

        try:
            temp = number_of_reviews.split()
            reviews = temp[-2].strip()
            reviews = reviews.replace(',', '')
            print(f" the reviews are {reviews}")
        except IndexError:
            reviews = "0"
            print(f" the reviews are {reviews}")
    except AttributeError:
        reviews = "0"
        print(f" the reviews are {reviews}")
    return reviews


def parse_data():

    count = 0

    for url in url_list:

        count = count + 1
        print(count)
        print(url)

        new_page = requests.get(url)

        if new_page.status_code == 200:

            new_soup = BeautifulSoup(new_page.text, 'lxml')
            product_ratings_Data = get_product_ratings(new_soup)
            star_rating_data = get_star_rating(new_soup)
            product_review_data = get_reviews(new_soup)
            seller_rating_data = get_seller_rating(new_soup)
            seller_name_data = get_seller_name(new_soup)

            print(f"The count is {count}")

            all_elements.append(  # saving all elements to a list
                {

                    "Product_url": url,
                    "Number_of_ratings": product_ratings_Data,
                    "Number_of_reviews": product_review_data,
                    "Star_rating_of_the_product": star_rating_data,
                    "Seller_rating_Data": seller_rating_data,
                    "Seller_name": seller_name_data

                })

            keys = all_elements[0].keys()

            with open('mergev1.csv', 'w', newline='') as output_file:  # writing all elements to csv
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(all_elements)



        else:
            pass


parse_data()

print(len(all_elements))

end = time.time()
print(f"Total runtime of the program is {end - begin}")
