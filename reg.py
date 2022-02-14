import re

import time

start_time = time.time()


def isphonenumber(text):
    phone_regex = re.compile(r'\d{4}')

    matching_object = phone_regex.findall(text)

    if matching_object is None:

        matched_text = " Pattern not found"

        print(matched_text)

    else:

        for i in range(len(matching_object)):
            matched_text = matching_object[i]

            print(matched_text)

    return matched_text


isphonenumber("The phone nymber is 2222 and what the hell is wrong with 333 and 4654")

end = time.time()

print(end - start_time)
