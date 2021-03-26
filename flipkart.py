import requests

from bs4 import BeautifulSoup

import re

import csv

base_url = "https://www.flipkart.com/search?q=washing+machine&page="

pagination_urls = []  # the products are listed in n mumber of pages and the urls to be stored in this list

product_urls = []  # the urls to individual products

all_elements = []


def generate_page_url():  # function to generate the pagination urls and save it to the list pagination urls

    count = 0

    while count < 32:
        page_url = base_url + str(count)

        print(page_url)

        pagination_urls.append(page_url)

        print(count)

        count = count + 1

generate_page_url()


def get_urls():
    for page in pagination_urls:

        response = requests.get(page)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'lxml')

            for link in soup.find_all('a', attrs={'class': '_1fQZEK'}):

                item_url = " https://www.flipkart.com" + link.get('href')

                item_url = re.split("\&", item_url)

                item_url = item_url[0]

                product_urls.append(item_url)

                upc = re.split("\=", item_url)
                upc = upc[-1]
                upc = upc.replace(',', '')

                try:
                    mrp = link.find('div', attrs={'class': '_3I9_wc _27UcVY'}).text.strip()  # the code to extract mrp
                    mrp = re.split("\₹", mrp)
                    mrp = mrp[-1]
                    mrp = mrp.replace(',', '')

                except Exception as e:

                    mrp = "mrp not available"

                try:

                    discount = link.find('div', attrs={'class': '_3Ay6Sb'}).text.strip()
                    discount = re.findall(r'\d+', discount)
                    discount = discount[0]

                except Exception as e:

                    discount = 0

                try:  # extracting element name

                    name = link.find('div', attrs={'class': '_4rR01T'}).text

                    brand = name.split()

                    brand = brand[0]

                except Exception as e:

                    name = "name not available"

                try:  # extracting element price from thw website
                    price = link.find('div', attrs={'class': '_30jeq3 _1_WHN1'}).text.strip()
                    price = re.split("\₹", price)
                    price = price[-1]
                    price = price.replace(',', '')

                except Exception as e:

                    price = "price not available"

                try:
                    rating = link.find('div', attrs={'class': '_3LWZlK'}).text.strip()

                except Exception as e:

                    rating = "raing not available"

                try:

                    reviews_and_ratings = link.find('span', attrs={'class': '_2_R_DZ'}).text
                    temp = reviews_and_ratings.split()
                    ratings = temp[0].strip()
                    ratings = ratings.replace(',', '')
                    reviews = temp[-2].strip()
                    reviews = reviews.replace(',', '')


                except Exception as e:

                    # number_of_ratings = " Ratings not available"
                    ratings = 0
                    reviews = 0

                try:

                    load_type = link.find('li', attrs={'class': 'rgWa7D'}).text.strip()

                except Exception as e:

                    load_type = "Unknown"

                try:
                    star_rating = link.find('div', attrs={'class': '_3LWZlK'}).text.strip()
                    star_rating = star_rating.replace(',', '')

                except Exception as e:

                    star_rating = 0

                print(item_url)
                print(name)
                print(price)
                print(rating)
                print(reviews_and_ratings)
                print(mrp)
                print(discount)
                print(brand)
                print(ratings)
                print(reviews)
                print(f"load type is {load_type}")
                print(f"the upc is {upc}")
                print(f"start raing is {star_rating}")

                all_elements.append(  # saving all elements to a list
                    {
                        "Product_name": name,
                        "Product_url": item_url,
                        "brand": brand,
                        "Sale_price": price,
                        "MRP": mrp,
                        "Discount_percentage": discount,
                        "Number_of_ratings": ratings,
                        "Number_of_reviews": reviews,
                        "Type_of_washing": load_type,
                        "UPC": upc,
                        "Star_rating": star_rating

                    }
                )

                keys = all_elements[0].keys()

                with open('washing_machines_fk_v2.csv', 'w', newline='') as output_file:  # writing all elements to csv
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(all_elements)




        else:

            pass


get_urls()