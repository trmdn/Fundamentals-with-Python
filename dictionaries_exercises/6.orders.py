orders = {}
command = input()

while command != "buy":
    command = command.split()
    name = command[0]
    price = float(command[1])
    quantity = int(command[-1])
    quantity_left = 0
    if name not in orders:
        orders[name] = {}
        orders[name][price] = 0
    else:
        quantity_left = list(orders[name].values())
        quantity_left = quantity_left[0]
        orders[name].clear()
        orders[name] = {}
        orders[name][price] = 0

    orders[name][price] += quantity + quantity_left
    command = input()

for i in orders:
    for keys, values in orders[i].items():
        result = keys * values
        print(f"{i} -> {result:.2f}")