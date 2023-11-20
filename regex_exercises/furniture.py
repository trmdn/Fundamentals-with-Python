import re

bought_furniture = []
total_price = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quality = match.groups()
        bought_furniture.append(furniture)
        total_price += float(price) * int(quality)
    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")