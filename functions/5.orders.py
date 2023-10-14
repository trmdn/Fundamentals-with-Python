# •	coffee - 1.50 water - 1.00 coke - 1.40 snacks - 2.00


def coffe_shop(name, number):
    if name == "coffee":
        price = 1.50
    elif name == "water":
        price = 1.00
    elif name == "coke":
        price = 1.40
    elif name == "snacks":
        price = 2.00
    result = price * number
    return result


orders = input()
quantity = int(input())
print(coffe_shop(number))
