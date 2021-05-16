import requests

from bs4 import BeautifulSoup

import re

import csv


url = 'https://www.mohfw.gov.in//' # the base URL for scrapping data

# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []

# soup.find_all('td') will scrape every
# element in the url's table
#data_iterator = iter(soup.find_all('td'))

# data_iterator is the iterator of the table
# This loop will keep repeating till there is
# data available in the iterator
#while True:
    #try:
        state = next(data_iterator).text
        active_cases = next(data_iterator).text
        change_in_active_cases = next(data_iterator).text
        total_active_cases = next(data_iterator).text
        change_in_total_active_cases = next(data_iterator).text
        total_deaths = next(data_iterator).text

        print(f"the state is  {state}")
        print(f"the active number of cases is  {active_cases}")
        print(f"the change in active  cases is  {change_in_active_cases}")

        # For 'confirmed' and 'deaths',
        # make sure to remove the commas
        # and convert to int
        data.append(
            {
                "State": state,
                "Active_cases": active_cases,
                "Change_in_active_cases": change_in_active_cases,
                "Total_Active_cases": total_active_cases,
                "Change_in_cumulative_active_cases": change_in_total_active_cases,
                "Total_deaths": total_deaths

            })

        keys = data[0].keys()
        with open('covid.csv', 'w', newline='') as output_file:  # writing all elements to csv
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)



    # StopIteration error is raised when
    # there are no more elements left to
    # iterate through
    except StopIteration:
        break


