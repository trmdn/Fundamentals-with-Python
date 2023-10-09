def is_even_number(num):
    return num % 2 == 0


number_as_strings = input().split()
number_as_digits = []

for number in number_as_strings:
    number_as_digits.append(int(number))

even_nums = []

for element in number_as_digits:
    if is_even_number(element):
        even_nums.append(element)

print(even_nums)