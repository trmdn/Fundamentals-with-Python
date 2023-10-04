multiple = int(input())
numbers_count = int(input())
list_with_numbers = []

for multiplier in range(1, numbers_count + 1):
    list_with_numbers.append(multiple * multiplier)
print(list_with_numbers)