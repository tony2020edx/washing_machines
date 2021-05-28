import pandas as pd


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


df = pd.read_csv('headphonesV1.csv')
df = df['Battery life']

df['Battery life'] = df[clean_battery_string(['Battery life'])]
df.to_csv('headphonesV1.csv')