def calculate_total_price(prod, count):
    if prod == "coffee":
        return f'{1.50 * count:.2f}'
    elif prod == "coke":
        return f'{1.40 * count:.2f}'
    elif prod == "water":
        return f'{1.00 * count:.2f}'
    elif prod == "snacks":
        return f'{2.00 * count:.2f}'


product = input()
quantity = int(input())
result = calculate_total_price(product, quantity)
print(result)