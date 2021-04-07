import csv
import re

import requests
from bs4 import BeautifulSoup

base_url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&sort=price_asc&p%5B%5D=facets.type%255B%255D%3DSmartphones&page="

search_page_url_list = []

product_url_list = []

all_fields = []


def generate_search_page_url():  # function to generate the pagination urls and save it to the list pagination urls

    count = 0

    while count < 3:
        page_url = base_url + str(count)  # generating the url

        print(page_url)

        search_page_url_list.append(page_url)  # append to the list pagination urls

        print(f"the scraped page count is {count}")

        count = count + 1


generate_search_page_url()


def get_data():
    for page in search_page_url_list:

        response = requests.get(page)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'lxml')

            for link in soup.find_all('a', attrs={'class': '_1fQZEK'}):
                item_url = " https://www.flipkart.com" + link.get('href')

                item_url = re.split("\&", item_url)

                item_url = item_url[0]

                product_url_list.append(item_url)

                print(f"The product url is {item_url}")
                print(len(product_url_list))

                upc = re.split("\=", item_url)
                upc = upc[-1]
                upc = upc.replace(',', '')
                print(f"The upc is {upc}")

                try:
                    mrp = link.find('div', attrs={'class': '_3I9_wc _27UcVY'}).text.strip()  # the code to extract mrp
                    mrp = re.split("\₹", mrp)
                    mrp = mrp[-1]
                    mrp = mrp.replace(',', '')
                    print(f"The mrp is {mrp}")

                except Exception as e:

                    mrp = 0

                try:

                    discount = link.find('div', attrs={'class': '_3Ay6Sb'}).text.strip()
                    discount = re.findall(r'\d+', discount)
                    discount = discount[0]
                    print(f"The discount is {discount}")

                except Exception as e:

                    discount = 0

                try:  # extracting element name

                    name = link.find('div', attrs={'class': '_4rR01T'}).text

                    brand = name.split()

                    brand = brand[0]

                    print(f"The brand name is {brand}")


                except Exception as e:

                    brand = "brand not available"
                    name = "name not available"

                try:  # extracting element price from thw website
                    price = link.find('div', attrs={'class': '_30jeq3 _1_WHN1'}).text.strip()
                    price = re.split("\₹", price)
                    price = price[-1]
                    price = price.replace(',', '')
                    print(f"The price is {price}")


                except Exception as e:

                    price = "price not available"

                try:
                    star_rating = link.find('div', attrs={'class': '_3LWZlK'}).text.strip()
                    print(f"the star rating is {star_rating}")


                except Exception as e:

                    star_rating = "raing not available"

                try:

                    reviews_and_ratings = link.find('span', attrs={'class': '_2_R_DZ'}).text
                    temp = reviews_and_ratings.split()
                    ratings = temp[0].strip()
                    ratings = ratings.replace(',', '')
                    reviews = temp[-2].strip()
                    reviews = reviews.replace(',', '')

                    print(f"the number of ratings  is {ratings}")
                    print(f"the number of reviews  is {reviews}")




                except Exception as e:

                    # number_of_ratings = " Ratings not available"
                    ratings = 0
                    reviews = 0

                try:

                    description = []




                    for desc in link.find_all('li', attrs={'class': 'rgWa7D'}):

                        desc = desc.text

                        desc = desc.replace('|', '')

                        description.append(desc)


                    print(description)






                except Exception as e:

                    description = "not available"

                all_fields.append(  # saving all elements to a list
                    {
                        "Product_name": name,
                        "Product_url": item_url,
                        "brand": brand,
                        "Sale_price": price,
                        "MRP": mrp,
                        "Discount_percentage": discount,
                        "Number_of_ratings": ratings,
                        "Number_of_reviews": reviews,
                        "UPC": upc,
                        "Star_rating": star_rating,
                        "product_description": description,
                        "Battery_capacity":battery,
                        "Ram": ram,

                    })

                keys = all_fields[0].keys()

                with open('testdatav5.csv', 'w', newline='') as output_file:  # writing all elements to csv
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()

                    dict_writer.writerows(all_fields)


        else:
            pass


get_data()


