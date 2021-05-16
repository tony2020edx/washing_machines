import csv

reader = csv.reader(open("oximeter_data_second_extraction.csv", newline=None), delimiter=',')
writer = csv.writer(open("outputv25.csv", 'w'), delimiter=';')
writer.writerows(reader)
