import csv

def clean_battery_string(input_string):

    if "hrs" in input_string:

        clean_string = input_string.replace("hrs", '')
        print(clean_string)
    elif "hr" in input_string:
        clean_string = input_string.replace("hr", '')
        print(clean_string)
    else:
        clean_string = input_string
        print(clean_string)

    return clean_string

data_to_save = []

with open('headphonesV1.csv', newline='') as csvfile:
   spamreader = csv.reader(csvfile)
   for row in spamreader:
       row[21] = clean_battery_string(row[21])
       data_to_save.append(row[21])
       print(row[1])

with open('hpout.csv', mode='w', newline='') as csv_file:
  csv_writer = csv.DictWriter(csv_file, fieldnames=['Battery', 'Product_url'])
  csv_writer.writeheader()
  for row in data_to_save:
    csv_writer.writerow(row)


