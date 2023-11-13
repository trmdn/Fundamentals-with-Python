numbers = input().split()
opposite_numbers = []

for number in numbers:
    number_as_integer = -int(number)
    opposite_numbers.append(number_as_integer)
print(opposite_numbers)