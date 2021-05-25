import requests

from bs4 import BeautifulSoup

import re

import csv

import time

begin = time.time()

base_url = ["https://www.flipkart.com/sony-wh-ch510-google-assistant-enabled-bluetooth-headset/p/itm4c2d049ea4e74?pid=ACCFKYCBAETWPBZX",
            "https://www.flipkart.com/boat-bassheads-103-blue-wired-headset/p/itm21547b132f2a3?pid=ACCFGYHHKJ94GN6A",
            "https://www.flipkart.com/jbl-c150si-wired-headset/p/itme30a606bdfa6b?pid=ACCEHDJBEJSQYYKU",
            "https://www.flipkart.com/jabra-elite-active-75t-noise-cancellation-enabled-bluetooth-headset/p/itm692cf3c604b25?pid=ACCFPU9YFPQPQVZB",
            "https://www.flipkart.com/zebronics-zeb-symphony-bluetooth-headset/p/itma31142ddccd37?pid=ACCFGAAGPGGTMQVB",
            "https://www.flipkart.com/sennheiser-pc-8-usb-wired-headset/p/itm725f8c6c51662?pid=ACCDAYUJDUWRJEDX",
            "https://www.flipkart.com/apple-airpods-pro-wireless-charging-case-active-noise-cancellation-enabled-bluetooth-headset/p/itmf54912ef1bd8b?pid=ACCFHYJ8ZU9WDHDW",
            "https://www.flipkart.com/beats-flex-bluetooth-headset/p/itmdf07c37903f23?pid=ACCFY7EHZDU2YVSF&lid=LSTACCFY7EHZDU2YVSFFWBB8K",
            "https://www.flipkart.com/skullcandy-uproar-bluetooth-headset-mic/p/itmc64b5973674db?pid=ACCEAY5FXE76HJVJ&lid=LSTACCEAY5FXE76HJVJQHWHIS",
            "https://www.flipkart.com/bose-quitecomfort-earbuds-bluetooth-headset/p/itm2496279be74bc?pid=ACCFVDF7QG4QJZV6"]




def get_title(soup):  # function to extract title #tested ok
    try:
        title = soup.find('span', attrs={'class': 'B_NuCI'}).text.strip()

        print(f" The is title {title}")

    except AttributeError:

        title = " Title not available"

    return title

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def get_specs(soup):#tested ok

    rows = soup.find_all('tr')
    clumns = soup.find_all('td')

    listofspecs = []

    for col in clumns:

        listofspecs.append(col.text.strip())

    print(listofspecs)

    dict_date = Convert(listofspecs)

    try:
        model_name = dict_date['Model Name']
        print(f" The model name is {model_name}")
    except Exception as e:
        model_name = "Not available"
        print(model_name)

    try:

        color = dict_date['Color']
        print(f"The color is {color}")

    except Exception as e:

        color = " Colour Not available"
        print(f"The color is {color}")

    try:
        Headphone_Type = dict_date['Headphone Type']
        print(f"The headphone type is {Headphone_Type}")

    except Exception as e:

        Headphone_Type = "Headphone type not available"
        print(f"The headphone type is {Headphone_Type}")

    try:

        Sweat_proof = dict_date['Sweat Proof']

        print(f" Sweat proof ? {Headphone_Type}")

    except Exception as e:

        Sweat_proof = "Not available"

        print(Sweat_proof)

    try:

        water_resistant = dict_date['Water Resistant']
        print(water_resistant)

    except Exception as e:

        water_resistant = "Not available"
        print(water_resistant)

    try:

        with_microphone = dict_date['With Microphone']

        print(with_microphone)

    except Exception as e:

        with_microphone = "Not available"
        print(with_microphone)

    try:

        connectivity = dict_date['Connectivity']

        print(connectivity)

    except Exception as e:

        connectivity = "Not available"
        print(connectivity)

    try:

        battery_life = dict_date['Battery Life']

        print(f"The battery lif is {battery_life} hours")

    except Exception as e:

        battery_life = "Not available"

        print(f"The battery life data not available")

def get_brand(soup): #tested and verified
    try:
        brand_name = soup.find('span', attrs={'class': 'B_NuCI'}).text
        brand = brand_name.split()
        brand = brand[0]
        print(f" The brand is {brand}")

    except AttributeError:
        brand = " Not Available"

    return brand


def get_mrp(soup): #tested ok
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


def get_sale_price(soup): #tested ok
    try:
        sale_price = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text.strip()
        sale_price = re.split("₹", sale_price)
        sale_price = sale_price[-1]
        sale_price = sale_price.replace(',', '')
        print(f"The sale_price is {sale_price}")

    except AttributeError:

        sale_price = "0"

    return sale_price


def get_discount(soup): #tested ok
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

def parse_data():

    for link in base_url:

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
