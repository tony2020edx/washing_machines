text = open("headphonesV1 copy.csv", "r")

# join() method combines all contents of
# csvfile.csv and formed as a string
text = ''.join([i for i in text])

# search and replace the contents
text = text.replace("hrs", "")
text = text.replace("hr", "")


# output.csv is the output file opened in write mode
x = open("headphonesV1 copy.csv", "w")

# all the replaced text is written in the output.csv file
x.writelines(text)
x.close()








