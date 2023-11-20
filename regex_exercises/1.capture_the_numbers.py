import re

input_string = input()

while input_string:
    pattern = r'\d+'

    matches = re.findall(pattern, input_string)

    if matches:
        print(" ".join(matches), end = " ")

    input_string = input()