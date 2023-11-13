number_cars = int(input())
parking_info = {}

def registered_car(name, number):
    if name in parking_info:
        print(f"ERROR: already registered with plate number")
    else:
        parking_info[name] = number
        print(f"{name} registered {number} successfully")

def unregistered_car(name):
    if name not in parking_info:
        print(f"ERROR: user {name} not found")
    else:
        del parking_info[name]
        print(f"{name} unregistered successfully")

def all_cars_in_parking():
    for key, value in parking_info.items():
        print(f"{key} => {value}")

for _ in range(number_cars):
    car = input()
    car = car.split()
    command = car[0]
    name = car[1]
    if command == "register":
        number = car[-1]
        registered_car(name, number)
    else:
        unregistered_car(name)

all_cars_in_parking()