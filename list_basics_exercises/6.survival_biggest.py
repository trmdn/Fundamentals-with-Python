numbers = input().split(" ")
list_of_numbers = []

for number in numbers:
    num_as_int = int(number)
    list_of_numbers.append(num_as_int)

nums_to_remove = int(input())
for i in range(nums_to_remove):
    list_of_numbers.remove(min(list_of_numbers))
print(*list_of_numbers, sep=", ")
