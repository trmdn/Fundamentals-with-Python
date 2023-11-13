data = input()
total_price = 0

special = 1

while data != "special" and data != "regular":
    price = float(data)

    if price > 0:
        total_price += price
    else:
        print("Invalid price!")

    data = input()

taxes = total_price * 0.2

if data == "special":
    special = 0.9

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {(total_price + taxes) * special:.2f}$")