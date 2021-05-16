import csv

def read_oxi():
    filename = open('mergev4.csv', 'r')

    file = csv.DictReader(filename, delimiter=';')

    for col in file:

        data = col['Product_url']

        writer = csv.writer(open("merge_cleaned.csv", 'w'), delimiter=';')
        writer.writerows(file)