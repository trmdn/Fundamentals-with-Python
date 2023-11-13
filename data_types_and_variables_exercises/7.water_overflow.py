number = int(input())
water_counter = 0
total_capacity = 255

for i in range(number):
    liters_of_water = int(input())
    if total_capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue
    total_capacity -= liters_of_water
    water_counter += liters_of_water
print(water_counter)

