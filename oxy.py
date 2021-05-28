import requests

from bs4 import BeautifulSoup

import re

import csv

import time

begin = time.time()

base_url = [
    "https://www.flipkart.com/search?q=pulse+oximeter&sid=zlw%2Cnyl%2Cbvv%2Cb5f&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_14_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_14_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=pulse+oximeter%7CPulse+Oximeters&requestId=79f2ffc9-48e8-4083-82bb-eed5c2f3640f&as-searchtext=pulse+oximeter&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1500&page=",
    "https://www.flipkart.com/search?q=pulse+oximeter&sid=zlw%2Cnyl%2Cbvv%2Cb5f&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_14_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_14_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=pulse+oximeter%7CPulse+Oximeters&requestId=79f2ffc9-48e8-4083-82bb-eed5c2f3640f&as-searchtext=pulse+oximeter&sort=price_desc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1500&page=",
    "https://www.flipkart.com/search?q=pulse+oximeter&sid=zlw%2Cnyl%2Cbvv%2Cb5f&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_14_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_14_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=pulse+oximeter%7CPulse+Oximeters&requestId=79f2ffc9-48e8-4083-82bb-eed5c2f3640f&as-searchtext=pulse+oximeter&sort=price_desc&p%5B%5D=facets.price_range.from%3D1500&p%5B%5D=facets.price_range.to%3DMax&page=",
]

pagination_urls = []  # here we generate pages by concatenating the urls

product_urls = []

all_elements = []  # all elements




def generate_page_url():  # function to generate the pagination urls and save it to the list pagination urls

    for i in range(len(base_url)):

        count = 0

        while count < 40:
            page_url = base_url[i] + str(count)  # generating the url

            print(page_url)

            pagination_urls.append(page_url)  # append to the list pagination urls

            print(count)

            count = count + 1


generate_page_url()


def get_data():  # function to get product page links

    for page in pagination_urls:

        response = requests.get(page)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'lxml')

            for link in soup.find_all('a', attrs={'class': 's1Q9rs'}):
                item_url = " https://www.flipkart.com" + link.get('href')

                item_url = re.split("&", item_url)

                item_url = item_url[0]

                print(f"The url is {item_url}")

                product_urls.append(item_url)


get_data()

unique_urls = set(product_urls)


def get_title(soup):  # function to extract title
    try:
        title = soup.find('span', attrs={'class': 'B_NuCI'}).text.strip()

        print(f" The is title {title}")

    except AttributeError:

        title = " Title not available"

    return title


def get_brand(soup):
    try:
        brand_name = soup.find('span', attrs={'class': 'B_NuCI'}).text
        brand = brand_name.split()
        brand = brand[0]
        print(f" The brand is {brand}")

    except AttributeError:
        brand = " Not Available"

    return brand


def get_mrp(soup):
    try:

        mrp = soup.find('div', attrs={'class': '_3I9_wc _2p6lqe'}).text.strip()
        mrp = re.split("₹", mrp)
        mrp = mrp[-1]
        mrp = mrp.replace(',', '')

        print(f"The mrp is {mrp}")

    except AttributeError:

        try:
            mrp = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text.strip()
            mrp = re.split("₹", mrp)
            mrp = mrp[-1]
            mrp = mrp.replace(',', '')

        except AttributeError:

            mrp = "0"

    return mrp


def get_sale_price(soup):
    try:
        sale_price = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text.strip()
        sale_price = re.split("₹", sale_price)
        sale_price = sale_price[-1]
        sale_price = sale_price.replace(',', '')
        print(f"The sale_price is {sale_price}")

    except AttributeError:

        sale_price = "0"

    return sale_price


def get_discount(soup):
    try:
        discount = soup.find('div', attrs={'class': '_3Ay6Sb _31Dcoz'}).text.strip()
        discount = re.findall(r'\d+', discount)
        discount = discount[0]
        print(f"The discount is {discount}")

    except AttributeError:
        discount = "0"
        print("DISCOUNT NOT AVAILABLE")

    return discount


def get_description(soup):
    try:
        description = soup.find('div', attrs={'class': '_2o-xpa'}).text.strip()
        print(f"The description is {description}")
    except AttributeError:
        description = "Description Not available"
        print(description)

    return description


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


def get_ratings(soup):
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


def get_star_rating(soup):
    try:

        star_rating = soup.find('div', attrs={'class': '_2d4LTz'}).text.strip()
        print(f" the star_rating is {star_rating}")

    except AttributeError:

        star_rating = "Not available"
        print(f" the star_rating is {star_rating}")

    return star_rating


def get_upc(link):
    try:

        upc = re.split("=", link)
        upc = upc[-1]
        upc = upc.replace(',', '')

        print(f"The upc is {upc}")

    except AttributeError:
        upc = "Not available"

    return upc

def get_assurence_data(soup):

    try:
        image_links = soup.find('img', attrs = {'class': 'jMnjzX'})
        src = image_links.get('src')
        print(f" The image link is {src}")
        flipkart_assured = "Yes"
        print(flipkart_assured)

    except AttributeError:

        flipkart_assured = "No"
        print(flipkart_assured)

    return flipkart_assured


def parse_data():
    for link in unique_urls:

        new_page = requests.get(link)

        if new_page.status_code == 200:

            new_soup = BeautifulSoup(new_page.text, 'lxml')

            title_data = get_title(new_soup)
            brand_data = get_brand(new_soup)
            mrp_data = get_mrp(new_soup)
            sale_price_data = get_sale_price(new_soup)
            discount_data = get_discount(new_soup)
            description_data = get_description(new_soup)
            seller_name_data = get_seller_name(new_soup)
            seller_rating_data = get_seller_star_rating(new_soup)
            ratings_data = get_ratings(new_soup)
            reviews_data = get_reviews_count(new_soup)
            star_ratings_data = get_star_rating(new_soup)
            upc_data = get_upc(link)
            flipkart_assurance = get_assurence_data(new_soup)

            all_elements.append(  # saving all elements to a list
                {

                    "Product_url": link,
                    "brand": brand_data,
                    "Title": title_data,
                    "Description": description_data,
                    "Sale_price": sale_price_data,
                    "MRP": mrp_data,
                    "Discount_percentage": discount_data,
                    "Seller_name": seller_name_data,
                    "seller_rating": seller_rating_data,
                    "Number_of_ratings": ratings_data,
                    "Number_of_reviews": reviews_data,
                    "UPC": upc_data,
                    "Star_rating_of_the_product": star_ratings_data,
                    "Flipkart Assurance": flipkart_assurance
                })

            keys = all_elements[0].keys()

            with open('oxymeters5.csv', 'w', newline='') as output_file:  # writing all elements to csv
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(all_elements)

        else:
            pass


parse_data()
print(len(product_urls))
print(len(unique_urls))
end = time.time()
print(f"Total runtime of the program is {end - begin}")
