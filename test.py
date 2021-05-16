import requests

from bs4 import BeautifulSoup

import csv


url_list = []

def read_oxi():

    filename = open('outputv15.csv', 'r')

    file = csv.DictReader(filename, delimiter=';')

    for col in file:

        url_list.append(col['Product_url'])

read_oxi()

def get_star_rating(soup):

    try:

        star_rating = soup.find('div', attrs={'class': '_2d4LTz'}).text.strip()
        print(f" the star_rating is {star_rating}")

    except AttributeError:

        star_rating = "0"
        print(f" the star_rating is {star_rating}")

    return star_rating



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
            print(f" the ratings are {ratings}")
    except AttributeError:
        ratings = "0"
        print(f" the ratings are {ratings}")

    return ratings

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


        for link in url_list:

            new_page = requests.get(i)

            if new_page.status_code == 200:

                new_soup = BeautifulSoup(new_page.text, 'lxml')
                product_ratings_Data = get_ratings(new_soup)
                star_rating_data = get_star_rating(new_soup)
                product_review_data = get_reviews(new_soup)





parse_data()



