import re

some_text = input()

all_digits = ''.join([x for x in some_text if x.isdigit()])
cool_threshold = 1
for number in all_digits:
    cool_threshold *= int(number)

patterns = re.compile(r"(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\1")
print(f"Cool threshold: {cool_threshold}")
result = list(re.finditer(patterns, some_text))
print(f"{len(result)} emojis found in the text. The cool ones are:")

for found in result:
    find_cool = 0
    for letter in found["emoji"]:
        find_cool += ord(letter)
    if find_cool >= cool_threshold:
        print(found[0])