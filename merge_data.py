import requests

from bs4 import BeautifulSoup

import csv

url_list = []

all_elements = []

import time

begin = time.time()


def read_oxi():
    filename = open('outputv15.csv', 'r')

    file = csv.DictReader(filename, delimiter=';')

    for col in file:
        url_list.append(col['Product_url'])


read_oxi()


def get_product_star_rating(soup):
    try:

        star_rating = soup.find('div', attrs={'class': '_2d4LTz'}).text.strip()
        print(f" the star_rating is {star_rating}")

    except AttributeError:

        star_rating = "0"
        print(f" the star_rating is {star_rating}")

    return star_rating


def get_product_ratings_count(soup):
    try:
        user_string = soup.find('span', attrs={'class': '_2_R_DZ'}).text

        user_string = user_string.split()


        ratings = user_string[0]

        print(f"the ratins are {ratings}")



    except AttributeError:

        ratings = "0"
        print(f" the rating of the product is  {ratings}")

    return ratings


def get_reviews_count(soup):
    try:

        user_string = soup.find('span', attrs={'class': '_2_R_DZ'}).text

        user_string = user_string.split()

        try:
            reviews = user_string[-2]

            print(f" the reviews are {reviews}")

        except IndexError:

            reviews = "131415"
            print(reviews)



    except AttributeError:

        reviews = "0"
        print(f" the review of the product is  {reviews}")

    return reviews


def get_seller_star_rating(soup):
    try:
        seller_string = soup.find('div', attrs={'class': '_3LWZlK _1D-8OL'}).text.strip()

        def convert(string):
            list1 = []
            list1[:0] = string
            return list1

        my_list = convert(seller_string)

        if '.' in my_list:

            seller_rating = my_list[-3] + '.' + my_list[-1]

            print(f"the seller_rating is a float {seller_rating}")

        else:

            seller_rating = my_list[-1]
            print(f" the seller_rating is integer {seller_rating}")


    except AttributeError:
        seller_rating = 0
        print(f"the rating is {seller_rating}")

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
    count = 0

    for url in url_list:

        print(url)

        new_page = requests.get(url)

        if new_page.status_code == 200:
            new_soup = BeautifulSoup(new_page.text, 'lxml')
            product_ratings_data = get_product_ratings_count(new_soup)
            star_rating_data = get_product_star_rating(new_soup)
            product_review_data = get_reviews_count(new_soup)
            seller_rating = get_seller_star_rating(new_soup)
            seller_name = get_seller_name(new_soup)

            count = count + 1
            print(f"THE ITEM COUNT is {count}")

            all_elements.append(  # saving all elements to a list
                {

                    "Product_url": url,
                    "Number_of_ratings": product_ratings_data,
                    "Number_of_reviews": product_review_data,
                    "Star_rating_of_the_product": star_rating_data,
                    "Seller_rating_Data": seller_rating,
                    "Seller_name": seller_name

                })

            keys = all_elements[0].keys()

            with open('mergev4.csv', 'w', newline='') as output_file:  # writing all elements to csv
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(all_elements)



        else:
            pass


parse_data()

print(len(all_elements))

end = time.time()
print(f"Total runtime of the program is {end - begin}")
