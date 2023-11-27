import re

information = input()
pattern = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
result = re.findall(pattern, information)
match_calories = sum([int(match[5]) for match in result])
days = match_calories // 2000
print(f"You have food to last you for: {days} days!")

for elements in result:
    item_name = elements[1]
    date = elements[3]
    expiration_date = elements[5]
    print(f"Item: {item_name}, Best before: {date}, Nutrition: {expiration_date}")