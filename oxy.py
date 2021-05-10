import requests

from bs4 import BeautifulSoup

import re

import csv

base_url = "https://www.flipkart.com/search?q=oxymeters&sid=zlw%2Cnyl%2Cbvv%2Cb5f&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=oxymeters%7CPulse+Oximeters&requestId=653e464f-738f-4258-a916-0c3af3cdbe98&page="

pagination_urls = []  # here we generate pages by concatenating the urls

product_urls = []  # the urls to individual products

all_elements = []


def generate_page_url():  # function to generate the pagination urls and save it to the list pagination urls

    count = 0

    while count < 1:

        page_url = base_url + str(count) #generating the url

        print(page_url)

        pagination_urls.append(page_url) #append to the list pagination urls

        print(count)

        count = count + 1

generate_page_url()


def get_data():  # function to parse data from each url generated in the generate url function

    for page in pagination_urls:

        response = requests.get(page)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'lxml')

            for link in soup.find_all('a', attrs={'class': 's1Q9rs'}):

                item_url = " https://www.flipkart.com" + link.get('href')

                item_url = re.split("\&", item_url)

                item_url = item_url[0]

                print(f"The url is {item_url}")

                product_urls.append(item_url)


get_data()


def get_title(soup):

    try:
        title = soup.find('span', attrs={'class': 'B_NuCI'}).text.strip()

        print(title)

    except AttributeError:

        title = ""

    return title

def get_brand(soup):

    try:
        brand_name = soup.find('span', attrs={'class': 'B_NuCI'}).text
        brand = brand_name.split()
        brand = brand[0]
        print(brand)

    except AttributeError:
        brand = " Not Available"

    return brand

def get_mrp(soup):

    try:

        mrp = soup.find('div', attrs={'class': '_3I9_wc _2p6lqe'}).text.strip()
        print(mrp)

    except AttributeError:

        mrp = ""

    return mrp

def get_sale_price(soup):

    try:
        sale_price = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text.strip()
        print(sale_price)

    except AttributeError:

        sale_price = "Not available"
    return sale_price

def get_discount(soup):

    try:
        discount = soup.find('div', attrs={'class': '_3Ay6Sb _31Dcoz'}).text.strip()
        print(discount)

    except AttributeError:
        discount = "0"

    return discount

def get_oxymeter_type(soup):

    try:
        oxymeter_type = soup.find('li', attrs = {'class': '_21lJbe'}).text.strip()
        print(oxymeter_type)

    except AttributeError:

        oxymeter_type = "Type not available"
    return oxymeter_type


def get_description(soup):

    try:
        description = soup.find('div', attrs = {'class': '_1mXcCf RmoJUa'}).text.strip()
        print(description)
    except AttributeError:
        description = "Description Not available"

    return description

def get_seller_name(soup):

    try:
        seller_name = soup.find('div', attrs = {'class': '_1RLviY'}).text.strip()
        print(seller_name)
    except AttributeError:
        seller_name = "Name Not available"

    return seller_name

def get_ratings(soup):

    try:
        number_of_ratings = soup.find('span', attrs = {'class': '_2_R_DZ'}).text
        temp = number_of_ratings.split()
        ratings = temp[0].strip()
        ratings = ratings.replace(',', '')
        print(f" the ratings are {ratings}")
    except AttributeError:
        ratings = "0"

    return ratings

def get_reviews(soup):

    try:
        number_of_reviews = soup.find('span', attrs = {'class': '_2_R_DZ'}).text
        temp = number_of_reviews.split()
        reviews = temp[-2].strip()
        reviews = reviews.replace(',', '')
        print(f" the reviews are {reviews}")
    except AttributeError:
        reviews = "0"
    return reviews

def get_star_rating(soup):

    try:

        star_rating = soup.find('div', attrs = {'class': '_3LWZlK'}).text.strip()
        print(f" the star_rating is {star_rating}")

    except AttributeError:

        star_rating = "Not available"

    return star_rating

def get_upc(link):

    try:

        upc = re.split("\=", link)
        upc = upc[-1]
        upc = upc.replace(',', '')

        print(f"The upc is {upc}")

    except AttributeError:
        upc = "Not available"

    return upc



def parse_data():

    for link in product_urls:

        new_page = requests.get(link)
        new_soup = BeautifulSoup(new_page.text, 'lxml')

        title_data = get_title(new_soup)
        brand_data = get_brand(new_soup)
        mrp_data = get_mrp(new_soup)
        sale_price_data = get_sale_price(new_soup)
        discount_data = get_discount(new_soup)
        oxymeter_type_data = get_oxymeter_type(new_soup)
        description_data = get_description(new_soup)
        seller_name_data = get_seller_name(new_soup)
        ratings_data = get_ratings(new_soup)
        reviews_data = get_reviews(new_soup)
        star_ratings_data = get_star_rating(new_soup)
        upc_data = get_upc(link)

        all_elements.append(  # saving all elements to a list
            {
                "Title": title_data,
                "Product_url": link,
                "brand": brand_data,
                "Description": description_data,
                "Sale_price": sale_price_data,
                "MRP": mrp_data,
                "Discount_percentage": discount_data,
                "Oxymeter_type": oxymeter_type_data,
                "Seller_name": seller_name_data,
                "Number_of_ratings": ratings_data,
                "Number_of_reviews": reviews_data,
                "UPC": upc_data,
                "Star_rating": star_ratings_data,
            })

        keys = all_elements[0].keys()

        with open('oxymeters1.csv', 'w', newline='') as output_file:  # writing all elements to csv
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(all_elements)




parse_data()



