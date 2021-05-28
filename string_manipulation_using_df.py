import pandas as pd

data = pd.read_csv("datacamp.csv")

battery = data['btr'].tolist()

upc = data['upc'].tolist()

price = data['mrp'].tolist()

print(battery)

def hasNumbers(inputString):

    return any(char.isdigit() for char in inputString)

def strip_string(input):

    stripped_number = ''.join(filter(str.isdigit, input))

    return stripped_number

for i in range(len(battery)):

    if hasNumbers(battery[i]) == True:

        clean = strip_string(battery[i])

        battery[i] = clean

    else:

        pass

print(battery)

dict = {'upc': upc, 'pricicing': price, 'battery_life': battery}

df = pd.DataFrame(dict)

df.to_csv('file1.csv')












