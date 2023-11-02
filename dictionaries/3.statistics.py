product_input = input()

product_in_stock = {}

while product_input != "statistics":
    product, quantity = product_input.split(": ")
    product_in_stock[product] = product_in_stock.get(product, 0 ) + int(quantity)
    product_input = input()

print("Products in stock:")

for product, quantity in product_in_stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(product_in_stock)}")
print(f"Total Quantity: {sum(product_in_stock.values())}")